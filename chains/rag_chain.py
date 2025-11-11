# chains/rag_chain.py
from tools.query_retrieval_layer import RetrievalTool
from prompts.qa_prompt import QA_PROMPT

# ====== RAG CHAIN ======
class RAGChain:
    def __init__(self, retriever: RetrievalTool, llm, output_parser=None):
        self.retriever = retriever
        self.llm = llm
        self.output_parser = output_parser

    def run(self, question: str, top_k: int = 5):
        # Retrieve context from the retriever
        docs = self.retriever.search_documents(question, top_k=top_k)
        context_text = "\n".join([d["text"] for d in docs])

        # Build the prompt
        prompt = QA_PROMPT.format(context=context_text, question=question)

        # Generate output using the LLM
        llm_output = self.llm.generate(prompt)

        # Optional parsing of the LLM output
        if self.output_parser:
            return self.output_parser.parse(llm_output)
        return llm_output