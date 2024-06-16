import os

from agents import SQLAgent
from prompts import QUESTION
from utils import setup_db

os.environ['OPENAI_API_KEY'] = "API KEY HERE"

if __name__ == "__main__":
    db_uri = setup_db()
    sql_agent = SQLAgent(db_uri)
    print(sql_agent.call(QUESTION))