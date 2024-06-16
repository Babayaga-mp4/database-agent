from llm import LLM

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.sql_database import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

from prompts import MSSQL_AGENT_FORMAT_INSTRUCTIONS, MSSQL_AGENT_PREFIX


class SQLAgent(LLM):
    def __init__(self, db_uri) -> None:
        super().__init__()
        self.db = SQLDatabase.from_uri(db_uri)
        self.toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)
        self.sql_agent = create_sql_agent(
                        prefix=MSSQL_AGENT_PREFIX,
                        format_instructions = MSSQL_AGENT_FORMAT_INSTRUCTIONS,
                        llm=self.llm,
                        toolkit=self.toolkit,
                        top_k=30,
                        verbose=True
                    )

    
    def call(self, message):
        return self.sql_agent(message)


class DataFrameAgent(LLM):
    def __init__(self, df) -> None:
        super().__init__()
        self.df_agent = create_pandas_dataframe_agent(llm=self.llm, df=df,verbose=True, allow_dangerous_code=True)
    
    def call(self, message):
        return self.df_agent(message)