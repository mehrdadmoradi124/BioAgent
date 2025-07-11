from langgraph.prebuilt import create_react_agent
from langchain.tools import tool
from langchain.chat_models import ChatOpenAI
import requests
import json
# ---------------- Agent 1: Extract keywords ----------------
agent1 = create_react_agent(
    model=ChatOpenAI(model="gpt-3.5-turbo"),
    tools=[],
    prompt="Extract relevant biomedical keywords from the user question."
)
