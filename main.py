import os

from llm import LLM
from prompts import HELLO_WORLD

os.environ['OPENAI_API_KEY'] = "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"

if __name__ == "__main__":
    llm_object = LLM()
    hello_world = llm_object.call(HELLO_WORLD)
    print(hello_world)