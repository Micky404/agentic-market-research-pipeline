import os
from agents import function_tool
from tavily import TavilyClient

@function_tool
def web_search_scraper(topic: str) -> str:
    """
    Crawls the live internet for up-to-date market updates, news, 
    and business data regarding a specific topic string.
    """
    # Initialize the client using your secure environment variable
    tavily_key = os.getenv("TAVILY_API_KEY")
    if not tavily_key:
        return "⚠️ Error: Missing TAVILY_API_KEY inside your .env configuration file."
    
    try:
        client = TavilyClient(api_key=tavily_key)
        
        # Execute a raw contextual internet search optimized for LLMs
        # include_answer=True tells the API to pre-synthesize a summary snippet
        response = client.search(
            query=topic, 
            search_depth="advanced", 
            max_results=3
        )
        
        # Clean and compile the results into raw text blocks for your agent
        raw_results = []
        for result in response.get("results", []):
            title = result.get("title", "No Title")
            url = result.get("url", "No URL")
            content = result.get("content", "")
            raw_results.append(f"[Source: {title} | {url}]\n{content}\n")
            
        compiled_text = "\n".join(raw_results)
        
        # Fallback if the internet search yielded completely empty returns
        if not compiled_text.strip():
            return f"Search completed, but no relevant market data could be retrieved for '{topic}'."
            
        return compiled_text

    except Exception as e:
        return f"❌ Live Scraper Error: Failed to fetch online data due to: {str(e)}"