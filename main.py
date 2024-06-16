import os
import pandas as pd

from llm import LLM
from agent import DataFrameAgent
from prompts import CSV_PROMPT_PREFIX, CSV_PROMPT_SUFFIX, HELLO_WORLD, HELLO_WORLD_AGENT, QUESTION

os.environ['OPENAI_API_KEY'] = ""

if __name__ == "__main__":
    # llm_object = LLM()
    # hello_world = llm_object.call(HELLO_WORLD)
    # print(hello_world)
    
    df = pd.read_csv("./data/all-states-history.csv").fillna(value = 0)
    agent_object = DataFrameAgent(df)
    # df_hello_world = agent_object.call(HELLO_WORLD_AGENT)
    # print(df_hello_world)
    print(agent_object.call(CSV_PROMPT_PREFIX + QUESTION + CSV_PROMPT_SUFFIX))