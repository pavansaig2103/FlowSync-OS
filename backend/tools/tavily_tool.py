from tavily import TavilyClient
from config import TAVILY_API_KEY

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing in environment variables")

client = TavilyClient(api_key=TAVILY_API_KEY)


def search_web(query: str):
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    # Extract clean results for agent use
    results = []

    for item in response.get("results", []):
        results.append({
            "title": item.get("title"),
            "url": item.get("url"),
            "content": item.get("content")
        })

    return results