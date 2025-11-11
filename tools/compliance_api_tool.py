# tools/compliance_api_tool.py
import requests
from utils.config import settings

# ====== CHECK A DOCUMENT OR TEXT AGAINST REGULATORY RULES VIA AN EXTERNAL API ======
class ComplianceApiTool:
    def check(self, text: str):
        response = requests.post(f"{settings.compliance_api_url}/check", json={"text": text})
        response.raise_for_status()
        return response.json()