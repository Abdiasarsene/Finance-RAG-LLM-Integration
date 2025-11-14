# src/core/llm_interface.py
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

# ====== GENERIC INTERFACE FOR INTERACTING WITH AN LLM ======
class LLMInterface(ABC):
    # Generates a complete response from the prompt
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        pass

    # Generates a streaming response
    @abstractmethod
    def stream_generate(self, prompt: str, **kwargs):
        pass

    # Counts the number of tokens used by the text
    @abstractmethod
    def count_tokens(self, text: str) -> int:
        pass

    # Returns the metadata for the model used
    @abstractmethod
    def get_model_info(self) -> Dict[str, Any]:
        pass