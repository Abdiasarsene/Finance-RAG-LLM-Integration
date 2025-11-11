# chains/summary_chain.py
from prompts.summary_prompt import SUMMARY_PROMPT

# ======= SUMMARY CHAIN ======
class SummaryChain:
    def __init__(self, llm, output_parser=None):
        self.llm = llm
        self.output_parser = output_parser

    # Documents: list of dicts, each containing a 'text' key
    def run(self, documents: list):
        # Combine all document texts into a single context
        context_text = "\n".join([doc["text"] for doc in documents])

        # Build the summary prompt
        prompt = SUMMARY_PROMPT.format(context=context_text)

        # Generate the summary using the LLM
        summary = self.llm.generate(prompt)

        # Optional parsing of the summary
        if self.output_parser:
            return self.output_parser.parse(summary)
        return summary