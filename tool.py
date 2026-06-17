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
        [Source: TechCrunch 2026] Small Language Models (SLMs) are eating the enterprise market. 
        Companies are shifting budget away from monolithic 1-trillion parameter APIs toward 
        on-premise 8B to 14B parameter models due to data privacy laws and token costs.
        [Source: Gartner 2026] Agentic workflow deployments grew by 240% year-over-year.
        """
    elif "ev" in topic_lower or "electric vehicle" in topic_lower:
        return """
        [Source: Reuters 2026] Solid-state battery production lines have hit 60% yield targets early. 
        Automakers are pivoting marketing strategies toward 800-mile ranges. 
        Traditional lithium-ion margins have shrunk by 14% globally.
        """
    else:
        return f"[Source: General Web Search] Found steady consumer interest regarding {topic}, but increasing customer acquisition costs across the sector."