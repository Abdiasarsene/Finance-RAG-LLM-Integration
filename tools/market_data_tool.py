# tools/market_data_tool.py
import requests
from utils.config import settings

# ====== FETCHE FINANCIAL MARKET DATA FROM EXTERNAL APIS  ======
class MarketDataTool:
    def get_stock_price(self, ticker: str):
        response = requests.get(f"{settings.market_data_api_url}/stocks/{ticker}")
        response.raise_for_status()
        return response.json()