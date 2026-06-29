# AI Research Agent

A CLI research assistant powered by Claude that searches the web and Wikipedia, then returns a structured summary you can save to disk.

## How it works

1. You enter a research query at the prompt
2. The agent uses web search (DuckDuckGo) and Wikipedia as needed
3. It returns a structured response: topic, summary, sources, and tools used
4. Optionally saves the output to `research_output.txt`

## Stack

- **LangChain 1.x** — agent orchestration via `create_agent`
- **Claude** (`claude-sonnet-4-6`) — the underlying LLM
- **ddgs** — DuckDuckGo web search
- **wikipedia** — Wikipedia summaries
- **Pydantic** — structured output schema

## Setup

**1. Clone and install dependencies**

```bash
git clone <repo-url>
cd ai-agent-python
pip install -r requirements.txt
```

**2. Set your Anthropic API key**

Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your_key_here
```

Get a key at [console.anthropic.com](https://console.anthropic.com).

**3. Run**

```bash
python main.py
```

You'll be prompted:

```
What can I help you research?
```

Enter any topic and the agent will produce a structured response like:

```
topic='Quantum computing' 
summary='...' 
sources=['https://...', '...'] 
tools_used=['search', 'wikipedia']
```

## Project structure

```
main.py        # Entry point — agent setup and query loop
tools.py       # Tool definitions: web search, Wikipedia, file save
requirements.txt
.env           # Not committed — add your API key here
```

## Adding tools

Define a function in [tools.py](tools.py) and wrap it with `Tool` from `langchain_core.tools`:

```python
from langchain_core.tools import Tool

def my_tool(query: str) -> str:
    ...

my_tool_instance = Tool(name="my_tool", func=my_tool, description="...")
```

Then add it to the `tools` list in [main.py](main.py).
