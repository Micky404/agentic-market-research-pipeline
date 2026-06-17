# main.py
import asyncio
from dotenv import load_dotenv
from agents import Runner
from agents_pool import triage_agent

# Automatically find and mount the local .env file variables
load_dotenv()

async def run_research_pipeline(user_target: str):
    print(f"🚀 Initializing Orchestrated Agent Pipeline for: '{user_target}'...\n")
    
    prompt = f"Please run a comprehensive market analysis report on the following industry sector: {user_target}"
    
    # Run the multi-agent orchestration
    result = await Runner.run(
        starting_agent=triage_agent, 
        input=prompt,
        max_turns=5 # Added safety cap to limit token usage!
    )
    
    print("\n--- Pipeline Execution Completed ---\n")
    print(f"Last Agent Active: {result.last_agent.name if result.last_agent else 'Unknown'}\n")
    print("📋 FINAL MARKET BRIEF OUTPUT:\n")
    print(result.final_output)
    
    # Save output to a markdown file
    with open("Market_Brief.md", "w", encoding="utf-8") as f:
        f.write(result.final_output)
    print("\n💾 File saved successfully as 'Market_Brief.md'")

if __name__ == "__main__":
    target_sector = "AI Enterprise Market Shifts"
    asyncio.run(run_research_pipeline(target_sector))