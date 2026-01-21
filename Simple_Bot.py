from typing import TypeDict, List
from langchain_core.message import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load.env()

Class AgentState(TypeDict):
