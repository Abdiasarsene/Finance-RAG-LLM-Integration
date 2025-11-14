# integration/data_models.py
from pydantic import BaseModel
from typing import List, Optional

# ====== SETTING ======
class RetrievalRequest(BaseModel):
    query: str
    top_k: int = 5

class Document(BaseModel):
    id: str
    content: str
    metadata: Optional[dict] = None

class RetrievalResponse(BaseModel):
    documents: List[Document]