# agents_pool.py
from agents import Agent, function_tool  # 💡 Added function_tool import
from tools import web_search_scraper

# Global storage variables (Gradio reads these)
triage_output = "No data yet..."
research_output = "No data yet..."
analyst_output = "No data yet..."

# 🟢 Wrap each logging function with the proper SDK decorator
@function_tool
def update_triage_log(text: str) -> str:
    """Updates the master tracking system with the triage agent's routing decision layout."""
    global triage_output
    triage_output = text
    return "Triage log storage updated successfully."

@function_tool
def update_research_log(text: str) -> str:
    """Saves the raw text blocks and scraped intelligence datasets into the master tracking system."""
    global research_output
    research_output = text
    return "Research log storage updated successfully."

@function_tool
def update_analyst_log(text: str) -> str:
    """Logs the extracted macro market shifts and key signals into the master tracking system."""
    global analyst_output
    analyst_output = text
    return "Analyst log storage updated successfully."

# --- REMINDER: MAKE SURE YOUR HANDOFFS ARE STILL SET UP SO THEY RUN CHRONOLOGICALLY ---

brief_writer_agent = Agent(
    name="brief_writer_agent",
    handoff_description="Specialist in formatting insights into markdown summaries.",
    instructions="Format the analyst findings into a pristine Markdown Market Research Brief.",
    model="gpt-4o"
)

trend_analyst_agent = Agent(
    name="trend_analyst_agent",
    handoff_description="Specialist in extracting trends from raw text data.",
    instructions="Identify the top macro trends. Call update_analyst_log with your findings, then handoff to brief_writer_agent.",
    tools=[update_analyst_log],
    handoffs=[brief_writer_agent],
    model="gpt-5.4-mini"
)

web_researcher_agent = Agent(
    name="web_researcher_agent",
    handoff_description="Specialist in scraping the internet.",
    instructions="Use web_search_scraper to gather raw text. Call update_research_log to save it, then handoff to trend_analyst_agent.",
    tools=[web_search_scraper, update_research_log],
    handoffs=[trend_analyst_agent],
    model="gpt-5.4-mini"
)

triage_agent = Agent(
    name="triage_agent",
    instructions="Determine user intent. Call update_triage_log to document your thoughts, then handoff to web_researcher_agent.",
    tools=[update_triage_log],
    handoffs=[web_researcher_agent],
    model="gpt-5.4-mini"
)