from langchain_groq import ChatGroq
from config import *

groq_llm = ChatGroq(
    model=GROQ_MODEL,
    temperature=TEMPERATURE
)