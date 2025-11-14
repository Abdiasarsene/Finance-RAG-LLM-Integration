# core/reasoning_orchestrator.py
from chains.rag_chain import RAGChain
from chains.summary_chain import SummaryChain
from chains.reporting_chain import ReportingChain

# ====== REASONING ORCHESTRATOR ======
class ReasoningOrchestrator:
    # Set up
    def __init__(self):
        self.chains = {
            "qa": RAGChain(),
            "summary": SummaryChain(),
            "reporting": ReportingChain()
        }

    # Selects the right chain and executes it
    def handle_query(self, query_type: str, context: dict):
        chain = self.chains.get(query_type)
        if not chain:
            raise ValueError(f"No chain configured for type: {query_type}")
        return chain.run(context)
