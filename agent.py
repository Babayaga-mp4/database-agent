from llm import LLM
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent


class DataFrameAgent(LLM):
    def __init__(self, df) -> None:
        super().__init__()
        self.df_agent = create_pandas_dataframe_agent(llm=self.llm, df=df,verbose=True, allow_dangerous_code=True)
    
    def call(self, message):
        return self.df_agent(message)

    

        