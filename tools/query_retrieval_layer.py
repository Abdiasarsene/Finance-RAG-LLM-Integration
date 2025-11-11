# tools/query_retrieval_layer.py
import requests
from utils.config import settings

class RetrievalTool:
    """
    Wraps the Retriever Layer API.
    Chains call this to fetch documents via HTTP, not directly from DBs or vectors.
    """
    def __init__(self):
        self.base_url = settings.retrieval_api_url

    def search_documents(self, query: str, top_k: int = 5):
        payload = {"query": query, "top_k": top_k}
        response = requests.post(f"{self.base_url}/search", json=payload)
        response.raise_for_status()
        return response.json()