"""Google Gemini API adapter."""

from google import genai
from google.genai import types

from .base import BaseAdapter, ModelResponse


class GeminiAdapter(BaseAdapter):
    """Adapter for Google Gemini models."""

    def __init__(self, api_key: str, model_id: str) -> None:
        """Initialize Gemini adapter."""
        super().__init__(api_key, model_id)
        self.client = genai.Client(api_key=api_key)

    @property
    def provider(self) -> str:
        """Return provider name."""
        return "google"

    def call(
        self,
        system_prompt: str,
        user_message: str,
        max_tokens: int = 4096,
        temperature: float = 0.7,
    ) -> ModelResponse:
        """
        Call Google Gemini model.

        Args:
            system_prompt: System instructions.
            user_message: User content to process.
            max_tokens: Maximum response tokens.
            temperature: Sampling temperature.

        Returns:
            ModelResponse with content and usage.
        """
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                max_output_tokens=max_tokens,
                temperature=temperature,
            ),
        )

        # Extract token counts from usage metadata
        input_tokens = 0
        output_tokens = 0
        if response.usage_metadata:
            input_tokens = response.usage_metadata.prompt_token_count or 0
            output_tokens = response.usage_metadata.candidates_token_count or 0

        content = ""
        if response.text:
            content = response.text

        return ModelResponse(
            content=content,
            model=self.model_id,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
        )
