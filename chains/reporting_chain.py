# chains/reporting_chain.py
class ReportingChain:
    """
    Combines outputs from multiple LLMs or chains
    and assembles a structured report.
    """

    def __init__(self, llms: dict, output_parser=None):
        """
        llms: dict[str, llm_instance] -> mapping of task names to LLM instances
        """
        self.llms = llms
        self.output_parser = output_parser

    def run(self, tasks: dict):
        """
        tasks: dict[str, str] -> {task_name: context_text}
        """
        results = {}

        # Iterate over all tasks and generate outputs
        for name, text in tasks.items():
            llm = self.llms.get(name)
            if not llm:
                continue
            output = llm.generate(text)

            # Optionally parse the output
            results[name] = self.output_parser.parse(output) if self.output_parser else output

        return results
