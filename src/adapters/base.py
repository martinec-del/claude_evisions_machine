"""Base adapter interface for AI models."""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ModelResponse:
    """Response from an AI model."""

    content: str
    model: str
    input_tokens: int
    output_tokens: int
    total_tokens: int


class BaseAdapter(ABC):
    """Abstract base class for AI model adapters."""

    def __init__(self, api_key: str, model_id: str) -> None:
        """Initialize adapter with API key and model ID."""
        self.api_key = api_key
        self.model_id = model_id

    @abstractmethod
    def call(
        self,
        system_prompt: str,
        user_message: str,
        max_tokens: int = 4096,
        temperature: float = 0.7,
    ) -> ModelResponse:
        """
        Call the AI model with a prompt.

        Args:
            system_prompt: System instructions for the model.
            user_message: User message/content to process.
            max_tokens: Maximum tokens in response.
            temperature: Sampling temperature.

        Returns:
            ModelResponse with content and usage statistics.
        """
        pass

    @property
    @abstractmethod
    def provider(self) -> str:
        """Return the provider name."""
        pass
