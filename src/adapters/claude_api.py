"""Anthropic Claude API adapter."""

from anthropic import Anthropic

from .base import BaseAdapter, ModelResponse


class ClaudeAdapter(BaseAdapter):
    """Adapter for Anthropic Claude models."""

    def __init__(self, api_key: str, model_id: str) -> None:
        """Initialize Claude adapter."""
        super().__init__(api_key, model_id)
        self.client = Anthropic(api_key=api_key)

    @property
    def provider(self) -> str:
        """Return provider name."""
        return "anthropic"

    def call(
        self,
        system_prompt: str,
        user_message: str,
        max_tokens: int = 4096,
        temperature: float = 0.7,
    ) -> ModelResponse:
        """
        Call Anthropic Claude model.

        Args:
            system_prompt: System instructions.
            user_message: User content to process.
            max_tokens: Maximum response tokens.
            temperature: Sampling temperature.

        Returns:
            ModelResponse with content and usage.
        """
        response = self.client.messages.create(
            model=self.model_id,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )

        # Extract content from response
        content = ""
        if response.content and len(response.content) > 0:
            content = response.content[0].text

        return ModelResponse(
            content=content,
            model=self.model_id,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            total_tokens=response.usage.input_tokens + response.usage.output_tokens,
        )
