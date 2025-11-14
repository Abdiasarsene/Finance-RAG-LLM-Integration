# core/reasoning_orchestrator.py
from chains.rag_chain import RAGChain
from chains.summary_chain import SummaryChain
from chains.reporting_chain import ReportingChain
from utils.logger import get_logger
from utils.monitoring import TOP_5_METRICS

# ====== CENTRAL BRAIN FOR SELECTING AND RUNNING CHAINS ======
class ReasoningOrchestrator:
    # Set up
    def __init__(self, context_builder):
        self.logger = get_logger(self.__class__.__name__)
        self.context_builder = context_builder

        # Register available chains
        self.chains = {
            "qa": RAGChain(),
            "summary": SummaryChain(),
            "reporting": ReportingChain()
        }

        # Initialize metrics storage (can be connected to Prometheus later)
        self.metrics = {metric: 0 for metric in TOP_5_METRICS}

    # Selects the chain, builds context, executes chain, and updates metrics
    def handle_query(self, query_type: str, user_id: str, retrieved_docs: list, extra_vars: dict = None):
        # Build context using ContextBuilder
        context = self.context_builder.build_context(user_id, retrieved_docs, extra_vars)

        # Log query handling start
        self.logger.info(f"Handling query for type '{query_type}' for user '{user_id}'")

        # Increment chain_execution_count metric
        self.metrics["chain_execution_count"] += 1
        self.metrics["retrieved_docs_count"] += len(retrieved_docs)

        # Execute the chain
        chain = self.chains.get(query_type)
        if not chain:
            self.metrics["chain_execution_failures"] += 1
            self.logger.error(f"No chain configured for type: {query_type}")
            raise ValueError(f"No chain configured for type: {query_type}")
        result = chain.run(context)
        
        # Increment LLM request metric (assuming each chain.run makes one LLM call)
        self.metrics["llm_request_count"] += 1
        self.logger.info(f"Query handled successfully for type '{query_type}'")

        return result