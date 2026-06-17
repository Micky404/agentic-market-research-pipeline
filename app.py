import asyncio
import gradio as gr
from dotenv import load_dotenv
from agents import Runner
# 1. MODIFICATION: Import the tracking variables from your pool
import agents_pool
from agents_pool import triage_agent

# Local fallback config for testing, won't conflict with Cloud setup
load_dotenv()

# 2. MODIFICATION: Removed -> str because we are now returning multiple pieces of text
async def analyze_market(target_sector: str):
    """
    Trigger function bound directly to the web interface submit button.
    Runs the OpenAI Agent SDK system asynchronously.
    """
    if not target_sector.strip():
        # Return blank entries for the logs if input is empty
        return "⚠️ Please provide a valid market category.", "", "", ""
    
    prompt = f"Please run a comprehensive market analysis report on the following industry sector: {target_sector}"
    
    try:
        # Run the multi-agent orchestration
        result = await Runner.run(
            starting_agent=triage_agent, 
            input=prompt,
            max_turns=12
        )
        
        # 3. MODIFICATION: Pull the captured data straight out of the pool variables!
        return (
            result.final_output, 
            agents_pool.triage_output, 
            agents_pool.research_output, 
            agents_pool.analyst_output
        )
    except Exception as e:
        error_msg = f"❌ An orchestration error occurred inside the system layer:\n{str(e)}"
        return error_msg, "Error", "Error", "Error"

# Custom HTML styling header to grab recruiter attention
header_html = """
<div style="text-align: center; max-width: 800px; margin: 0 auto; padding-top: 20px;">
    <h1 style="color: #2D3748; font-size: 2.2rem; font-weight: 700; margin-bottom: 0.5rem;">
        🏢 Multi-Agent Market Intelligence Hub
    </h1>
    <p style="color: #718096; font-size: 1.1rem;">
        Powered by OpenAI Agents SDK. Built with a specialized chain of 4 collaborative agents: 
        <strong>Triage Orchestrator ➔ Web Scraper ➔ Trend Analyst ➔ Executive Writer</strong>.
    </p>
</div>
"""

# Assemble the modern Gradio interface block layout
with gr.Blocks() as demo:
    gr.HTML(header_html)
    
    with gr.Row():
        with gr.Column(scale=1):
            input_box = gr.Textbox(
                label="Target Market / Industry Vertical",
                placeholder="e.g., Enterprise Small Language Models (SLMs) or Electric Vehicles Solid-State Batteries",
                lines=2
            )
            submit_btn = gr.Button("🚀 Execute Orchestration Pipeline", variant="primary")
            
            gr.Markdown("""
            ### 🧑‍💻 Engineering Architecture Notes
            * Each agent works with isolated task concerns.
            * Handoff operations are performed natively with JSON context passing.
            * Outputs are fully structured markdown documents ready for executive distribution.
            """)
            
            # 4. MODIFICATION: Added clean visual display blocks for each agent log
            gr.Markdown("### 📋 Individual Agent Workspace Outputs")
            triage_display = gr.Textbox(label="1. Triage Agent Log", placeholder="Waiting...")
            research_display = gr.Textbox(label="2. Web Researcher Log", placeholder="Waiting...")
            analyst_display = gr.Textbox(label="3. Trend Analyst Log", placeholder="Waiting...")
            
        with gr.Column(scale=2):
            output_markdown = gr.Markdown(
                label="Generated Intelligence Brief",
                value="*The compiled analyst document output will display here ONCE execution completes.*"
            )
            
    # 5. MODIFICATION: Map the button to output to all 4 UI boxes seamlessly
    submit_btn.click(
        fn=analyze_market,
        inputs=input_box,
        outputs=[output_markdown, triage_display, research_display, analyst_display]
    )

# Launch system block loop
if __name__ == "__main__":
    demo.queue().launch(theme=gr.themes.Soft(primary_hue="blue", secondary_hue="slate"))