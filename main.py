from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
# from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches for information based on a query and returns the result as a string.
#     Args:
#         query (str): The search query.
#     Returns:
#         The search result.
#     """
#     print(f"Searching for: {query}")
#     return tavily.search(query=query)

llm = ChatGroq(model="openai/gpt-oss-120b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)



def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="search fro 3 job openings for AI engineer in Langchain, in the Bay Area in Linkedin and also all the details here")})
    print(result)

if __name__ == "__main__":
    main()
