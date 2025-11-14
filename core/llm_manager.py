# src/core/llm_manager.py
import os
import time
from typing import Dict, Optional, List
from utils.logger import get_logger
from .llm_interface import LLMInterface

# ====== LOGGING ======
logger = get_logger(__name__)

# ====== CENTRALIZE LLM CLIENT MANAGEMENT AND FALLBACK BETWEEN MODELS ======
class LLMManager:
    # Set Up
    def __init__(self):
        self.clients: Dict[str, LLMInterface] = {}
        self.last_call: float = 0.0
        self.min_interval: float = 0.5  # seconds

    # Register Client
    def register_client(self, provider: str, client: LLMInterface):
        self.clients[provider.lower()] = client
        logger.info(f"✅ LLM client enregistré : {provider}")

    # Get Client
    def get_client(self, provider: str) -> Optional[LLMInterface]:
        client = self.clients.get(provider.lower())
        if not client:
            raise ValueError(f"Aucun client LLM trouvé pour '{provider}'")
        return client

    # Attempts several fallback providers
    def generate(self, providers: List[str], prompt: str, **kwargs) -> str:
        self._rate_limit()

        for provider in providers:
            try:
                client = self.get_client(provider)
                logger.info(f"🧠 Using provider: {provider}")
                return client.generate(prompt, **kwargs)
            except Exception as e:
                logger.warning(f"⚠️ {provider} failed: {e}. Trying next...")

        raise RuntimeError("🚨 All LLM providers failed!")

    # Rate Limit
    def _rate_limit(self):
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_call = time.time()