from langchain_core.tools import Tool
from datetime import datetime
import wikipedia
from ddgs import DDGS


def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data successfully saved to {filename}"


def search_web(query: str) -> str:
    results = DDGS().text(query, max_results=5)
    if not results:
        return "No results found."
    return "\n\n".join(f"{r['title']}\n{r['href']}\n{r['body']}" for r in results)


def search_wikipedia(query: str) -> str:
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0], sentences=2)
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{query}'."


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)

search_tool = Tool(
    name="search",
    func=search_web,
    description="Search the web for information.",
)

wiki_tool = Tool(
    name="wikipedia",
    func=search_wikipedia,
    description="Search Wikipedia for a concise summary on a topic.",
)
