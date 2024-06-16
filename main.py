import os

from agent import DataFrameAgent, SQLAgent
from prompts import CSV_PROMPT_PREFIX, CSV_PROMPT_SUFFIX, QUESTION
from utils import setup_db, DB_PATH

os.environ['OPENAI_API_KEY'] = "API KEY HERE"

if __name__ == "__main__":
    db_uri = setup_db()
    sql_agent = SQLAgent(db_uri)
    print(sql_agent.call(QUESTION))