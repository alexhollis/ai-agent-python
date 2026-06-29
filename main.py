from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatAnthropic(model_name="claude-sonnet-4-6", timeout=120, stop=None)

tools = [search_tool, wiki_tool, save_tool]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a research assistant that will help generate a research paper. "
        "Answer the user query and use necessary tools."
    ),
    response_format=ResearchResponse,
)

query = input("What can I help you research? ")
result = agent.invoke({"messages": [{"role": "user", "content": query}]})

structured_response = result.get("structured_response")
if structured_response:
    print(structured_response)
else:
    print(result["messages"][-1].content)
