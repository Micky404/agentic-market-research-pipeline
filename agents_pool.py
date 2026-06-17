from agents import Agent
from tools import web_search_scraper

# 1. Brief Writer Agent (The final output specialist)
brief_writer_agent = Agent(
    name="Brief_Writer_Agent",
    handoff_description="Specialist in formatting insights into a professional markdown executive summary.",
    instructions=(
        "You are an expert technical corporate writer. Take the trends provided by the analyst "
        "and draft a pristine, professional Markdown Market Research Brief. Organize it with "
        "Clear Headers, Executive Summaries, and actionable strategic takeaways."
    ),
    model="gpt-4o"
)

# 2. Trend Analyst Agent
trend_analyst_agent = Agent(
    name="Trend_Analyst_Agent",
    handoff_description="Specialist in processing raw text data to extract macroeconomic trends and shifts.",
    instructions=(
        "You are an elite Market Strategist. Analyze the raw data provided by the Web Research Agent. "
        "Identify the top macro trends, note counter-signals, and handoff your structured findings "
        "to the Brief Writer Agent to finalize the document."
    ),
    handoffs=[brief_writer_agent],
    model="gpt-4o"
)

# 3. Web Researcher Agent
web_researcher_agent = Agent(
    name="Web_Researcher_Agent",
    handoff_description="Specialist in using tools to scrape the internet for recent data.",
    instructions=(
        "You are a web parsing agent. Use the `web_search_scraper` tool to gather raw data on the target industry. "
        "Do not try to analyze the trends yourself. Once you gather the text, immediately handoff the execution "
        "to the Trend Analyst Agent."
    ),
    tools=[web_search_scraper],
    handoffs=[trend_analyst_agent],
    model="gpt-4o"
)

# 4. Triage / Router Agent (The Entry Point)
triage_agent = Agent(
    name="Triage_Agent",
    instructions=(
        "You are the orchestrator. Determine what industry or topic the user wants to research, "
        "and immediately route/handoff the task to the Web Researcher Agent to begin the workflow."
    ),
    handoffs=[web_researcher_agent],
    model="gpt-4o"
)