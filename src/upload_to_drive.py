"""Upload files to a Google Drive folder via service account.

Creates (or reuses) a named subfolder under the parent folder, then uploads
each file. If a file of the same name already exists in the subfolder, it is
replaced (drive.files().update) so reruns are idempotent.

Output: JSON on stdout with subfolder URL + per-file URLs.

Usage:
    python upload_to_drive.py \
        --folder-url "https://drive.google.com/drive/folders/ABC..." \
        --subfolder "seo-pro-e-commerce" \
        --files file1.xlsx file2.docx file3.html

Setup (one-time):
    1. Create (or reuse) a Google Cloud service account with the Drive API enabled.
    2. Place its JSON key at credentials/google_sheets.json (or set
       GOOGLE_SHEETS_CREDENTIALS in .env to a different path).
    3. Share the parent Drive folder with the service account's email (Editor role).
"""
import argparse
import json
import mimetypes
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive"]
FOLDER_MIME = "application/vnd.google-apps.folder"
MIME_OVERRIDES = {
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".html": "text/html",
    ".htm": "text/html",
    ".md": "text/markdown",
}
# Project-relative default; override via GOOGLE_SHEETS_CREDENTIALS env var
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
DEFAULT_CREDS = os.getenv(
    "GOOGLE_SHEETS_CREDENTIALS",
    str(PROJECT_ROOT / "credentials" / "google_sheets.json"),
)


def _service_account_email(creds_path: str) -> str:
    """Read client_email out of the service account JSON, for error messages."""
    try:
        data = json.loads(Path(creds_path).read_text(encoding="utf-8"))
        return data.get("client_email", "(unknown — check credentials file)")
    except Exception:
        return "(unknown — check credentials file)"


def parse_folder_id(url_or_id: str) -> str:
    """Extract folder ID from a Drive URL, or return bare ID if already provided."""
    m = re.search(r"/folders/([a-zA-Z0-9_-]+)", url_or_id)
    if m:
        return m.group(1)
    if re.fullmatch(r"[a-zA-Z0-9_-]{20,}", url_or_id.strip()):
        return url_or_id.strip()
    sys.exit(f"ERROR: cannot extract folder ID from: {url_or_id}")


def escape_for_query(name: str) -> str:
    """Escape single quotes for Drive query strings."""
    return name.replace("\\", "\\\\").replace("'", "\\'")


def get_or_create_subfolder(service, parent_id: str, name: str) -> dict:
    """Return existing subfolder by name under parent, or create a new one."""
    safe = escape_for_query(name)
    query = (
        f"'{parent_id}' in parents and name = '{safe}' "
        f"and mimeType = '{FOLDER_MIME}' and trashed = false"
    )
    res = service.files().list(
        q=query,
        fields="files(id,name,webViewLink)",
        supportsAllDrives=True,
        includeItemsFromAllDrives=True,
    ).execute()
    if res.get("files"):
        return res["files"][0]

    meta = {"name": name, "mimeType": FOLDER_MIME, "parents": [parent_id]}
    return service.files().create(
        body=meta,
        fields="id,name,webViewLink",
        supportsAllDrives=True,
    ).execute()


def find_existing_file(service, parent_id: str, name: str):
    """Return existing non-folder file with this name in parent, or None."""
    safe = escape_for_query(name)
    query = (
        f"'{parent_id}' in parents and name = '{safe}' "
        f"and mimeType != '{FOLDER_MIME}' and trashed = false"
    )
    res = service.files().list(
        q=query,
        fields="files(id,name)",
        supportsAllDrives=True,
        includeItemsFromAllDrives=True,
    ).execute()
    files = res.get("files", [])
    return files[0] if files else None


def upload_file(service, parent_id: str, path: Path) -> dict:
    """Upload (or replace) a single file into the parent folder."""
    mime = (
        MIME_OVERRIDES.get(path.suffix.lower())
        or mimetypes.guess_type(str(path))[0]
        or "application/octet-stream"
    )
    media = MediaFileUpload(str(path), mimetype=mime, resumable=False)

    existing = find_existing_file(service, parent_id, path.name)
    if existing:
        return service.files().update(
            fileId=existing["id"],
            media_body=media,
            fields="id,name,webViewLink",
            supportsAllDrives=True,
        ).execute()

    meta = {"name": path.name, "parents": [parent_id]}
    return service.files().create(
        body=meta,
        media_body=media,
        fields="id,name,webViewLink",
        supportsAllDrives=True,
    ).execute()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--folder-url", required=True,
                    help="Parent Drive folder URL or bare folder ID")
    ap.add_argument("--subfolder", required=True,
                    help="Name of subfolder to create (or reuse) under parent")
    ap.add_argument("--files", nargs="+", required=True,
                    help="Paths to files to upload")
    ap.add_argument("--credentials", default=DEFAULT_CREDS,
                    help=f"Path to service account JSON (default: {DEFAULT_CREDS})")
    args = ap.parse_args()

    file_paths = [Path(f) for f in args.files]
    for p in file_paths:
        if not p.exists():
            sys.exit(f"ERROR: file not found: {p}")

    if not Path(args.credentials).exists():
        sys.exit(f"ERROR: credentials file not found: {args.credentials}")

    creds = service_account.Credentials.from_service_account_file(
        args.credentials, scopes=SCOPES
    )
    service = build("drive", "v3", credentials=creds)

    parent_id = parse_folder_id(args.folder_url)
    service_account_email = _service_account_email(args.credentials)

    try:
        sub = get_or_create_subfolder(service, parent_id, args.subfolder)
        sub_url = sub.get("webViewLink") or (
            f"https://drive.google.com/drive/folders/{sub['id']}"
        )

        results = []
        for p in file_paths:
            up = upload_file(service, sub["id"], p)
            results.append({
                "name": up["name"],
                "id": up["id"],
                "url": up.get("webViewLink", f"https://drive.google.com/file/d/{up['id']}/view"),
            })

        out = {
            "subfolder_id": sub["id"],
            "subfolder_name": sub["name"],
            "subfolder_url": sub_url,
            "files": results,
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))

    except HttpError as e:
        status = getattr(e.resp, "status", None)
        if status == 404:
            sys.exit(
                f"ERROR: parent folder {parent_id} not accessible.\n"
                f"Did you share it with {service_account_email} (Editor)?"
            )
        if status == 403:
            sys.exit(
                f"ERROR: 403 from Drive API.\n"
                f"Likely the Drive API is not enabled in the Google Cloud project, "
                f"or the service account lacks Editor on the parent folder.\n"
                f"Detail: {e}"
            )
        raise


if __name__ == "__main__":
    main()
