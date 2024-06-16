from langchain_openai import ChatOpenAI

class LLM():
    def __init__(self) -> None:
        self.llm = ChatOpenAI(
                model="gpt-3.5-turbo-0125",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
            )
    def call(self, message):
        return self.llm.invoke([message]).content