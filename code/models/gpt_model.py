from langchain_openai import ChatOpenAI
from config import *

gpt_llm = ChatOpenAI(
    model=GPT_MODEL,
    temperature=0
)