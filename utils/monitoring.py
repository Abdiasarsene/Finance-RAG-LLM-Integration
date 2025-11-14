# core/monitoring.py

"""
Defines top 5 essential metrics for LLM Integration repo.
These are key to monitor performance, reliability, and usage.
"""

TOP_5_METRICS = [
    "llm_request_count",      # Number of LLM requests made
    "llm_request_latency_ms", # Latency per LLM request
    "chain_execution_count",  # Number of times each chain is executed
    "chain_execution_failures", # Count of failed chain runs
    "retrieved_docs_count"    # Number of documents retrieved per request
]
