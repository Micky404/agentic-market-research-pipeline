from agents import function_tool

@function_tool
def web_search_scraper(topic: str) -> str:
    """
    Simulates crawling the web for live market updates on a specific topic.
    Returns unstructured web text data.
    """
    topic_lower = topic.lower()
    
    if "ai" in topic_lower or "artificial intelligence" in topic_lower:
        return """
        [Source: TechCrunch 2026] Small Language Models (SLMs) are eating the enterprise market...
        """
    elif "ev" in topic_lower or "electric vehicle" in topic_lower:
        return """
        [Source: Reuters 2026] Solid-state battery production lines have hit 60% yield targets early. 
        Automakers are pivoting marketing strategies toward 800-mile ranges. 
        Traditional lithium-ion margins have shrunk by 14% globally.
        """
    else:
        return f"[Source: General Web Search] Found steady consumer interest regarding {topic}, but increasing customer acquisition costs across the sector."