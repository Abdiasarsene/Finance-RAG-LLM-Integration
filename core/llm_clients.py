# src/core/llm_clients.py
import os
from openai import OpenAI
from .llm_interface import LLMInterface

# ====== OPENAI ======
class OpenAIClient(LLMInterface):
    # Set up
    def __init__(self, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model

    # Generate
    def generate(self, prompt: str, **kwargs) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        return completion.choices[0].message.content

    # Stream Generate
    def stream_generate(self, prompt: str, **kwargs):
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            **kwargs
        )
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    # Count tokens
    def count_tokens(self, text: str) -> int:
        return len(text.split())

    # Get model info
    def get_model_info(self):
        return {"provider": "openai", "model": self.model}


# ====== ANTHROPIC ======
class AnthropicClient(LLMInterface):
    # Set Up
    def __init__(self, model: str = "claude-3-opus"):
        self.model = model
        self.api_key = os.getenv("ANTHROPIC_API_KEY")

    # Generate
    def generate(self, prompt: str, **kwargs) -> str:
        return f"[Claude simulated response to: {prompt}]"

    # Stream Generate
    def stream_generate(self, prompt: str, **kwargs):
        yield "[Claude simulated streaming...]"

    # Count Tokens
    def count_tokens(self, text: str) -> int:
        return len(text.split())

    # Get Model Info
    def get_model_info(self):
        return {"provider": "anthropic", "model": self.model}


# ====== MISTRAL ======
class MistralClient(LLMInterface):
    # Set Up
    def __init__(self, model: str = "mistral-large"):
        self.model = model
        self.api_key = os.getenv("MISTRAL_API_KEY")

    # Generate
    def generate(self, prompt: str, **kwargs) -> str:
        return f"[Mistral simulated response to: {prompt}]"

    # Stream Generate
    def stream_generate(self, prompt: str, **kwargs):
        yield "[Mistral simulated streaming...]"

    # Count Tokens
    def count_tokens(self, text: str) -> int:
        return len(text.split())

    # Get Model Info
    def get_model_info(self):
        return {"provider": "mistral", "model": self.model}