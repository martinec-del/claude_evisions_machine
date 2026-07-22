"""OpenAI API adapter for GPT models."""

from openai import OpenAI

from .base import BaseAdapter, ModelResponse


class OpenAIAdapter(BaseAdapter):
    """Adapter for OpenAI GPT models."""

    def __init__(self, api_key: str, model_id: str) -> None:
        """Initialize OpenAI adapter."""
        super().__init__(api_key, model_id)
        self.client = OpenAI(api_key=api_key)

    @property
    def provider(self) -> str:
        """Return provider name."""
        return "openai"

    def call(
        self,
        system_prompt: str,
        user_message: str,
        max_tokens: int = 4096,
        temperature: float = 0.7,
    ) -> ModelResponse:
        """
        Call OpenAI GPT model.

        Args:
            system_prompt: System instructions.
            user_message: User content to process.
            max_tokens: Maximum response tokens.
            temperature: Sampling temperature.

        Returns:
            ModelResponse with content and usage.
        """
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        usage = response.usage
        return ModelResponse(
            content=response.choices[0].message.content or "",
            model=self.model_id,
            input_tokens=usage.prompt_tokens if usage else 0,
            output_tokens=usage.completion_tokens if usage else 0,
            total_tokens=usage.total_tokens if usage else 0,
        )
