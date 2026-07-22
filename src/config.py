"""Configuration and API key management."""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from dotenv import load_dotenv


@dataclass
class ModelConfig:
    """Configuration for a single AI model."""

    name: str
    provider: str
    model_id: str
    max_tokens: int = 4096
    temperature: float = 0.7


# Load environment variables
load_dotenv()


@dataclass
class Config:
    """Application configuration."""

    # API Keys
    openai_api_key: str = field(default_factory=lambda: os.getenv("OPENAI_API_KEY", ""))
    google_api_key: str = field(default_factory=lambda: os.getenv("GOOGLE_API_KEY", ""))
    anthropic_api_key: str = field(
        default_factory=lambda: os.getenv("ANTHROPIC_API_KEY", "")
    )
    marketing_miner_api_key: str = field(
        default_factory=lambda: os.getenv("MARKETING_MINER_API_KEY", "")
    )

    # Paths
    project_root: Path = field(
        default_factory=lambda: Path(__file__).parent.parent.resolve()
    )

    # Model configurations
    models: dict[str, ModelConfig] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Initialize model configurations."""
        self.models = {
            "gpt-4o": ModelConfig(
                name="GPT-4o",
                provider="openai",
                model_id="gpt-4o",
                max_tokens=4096,
                temperature=0.7,
            ),
            "gpt-4o-mini": ModelConfig(
                name="GPT-4o Mini",
                provider="openai",
                model_id="gpt-4o-mini",
                max_tokens=4096,
                temperature=0.7,
            ),
            "gpt-5-mini": ModelConfig(
                name="GPT-5 Mini",
                provider="openai",
                model_id="gpt-5-mini",
                max_tokens=9000,
                temperature=0.7,
            ),
            "gemini-2.5-flash": ModelConfig(
                name="Gemini 2.5 Flash",
                provider="google",
                model_id="gemini-2.5-flash",
                max_tokens=9000,
                temperature=0.7,
            ),
            "claude-sonnet-4-6": ModelConfig(
                name="Claude Sonnet 4.6",
                provider="anthropic",
                model_id="claude-sonnet-4-6",
                max_tokens=9000,
                temperature=0.7,
            ),
            "gemini-2.0-flash": ModelConfig(
                name="Gemini 2.0 Flash",
                provider="google",
                model_id="gemini-2.0-flash",
                max_tokens=4096,
                temperature=0.7,
            ),
            "claude-3-5-sonnet": ModelConfig(
                name="Claude 3.5 Sonnet",
                provider="anthropic",
                model_id="claude-sonnet-4-20250514",
                max_tokens=4096,
                temperature=0.7,
            ),
        }

    @property
    def prompts_dir(self) -> Path:
        """Path to prompts directory."""
        return self.project_root / "prompts"

    @property
    def output_dir(self) -> Path:
        """Path to output directory."""
        return self.project_root / "data" / "output" / "tests"

    def get_api_key(self, provider: str) -> str:
        """Get API key for provider."""
        keys = {
            "openai": self.openai_api_key,
            "google": self.google_api_key,
            "anthropic": self.anthropic_api_key,
            "marketing_miner": self.marketing_miner_api_key,
        }
        key = keys.get(provider, "")
        if not key:
            raise ValueError(f"API key not found for provider: {provider}")
        return key

    def validate(self) -> dict[str, bool]:
        """Check which API keys are configured."""
        return {
            "openai": bool(self.openai_api_key),
            "google": bool(self.google_api_key),
            "anthropic": bool(self.anthropic_api_key),
            "marketing_miner": bool(self.marketing_miner_api_key),
        }


# Global config instance
config = Config()
