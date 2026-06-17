import asyncio
import gradio as gr
from dotenv import load_dotenv
from agents import Runner
from agents_pool import triage_agent

# Local fallback config for testing, won't conflict with Cloud setup
load_dotenv()

async def analyze_market(target_sector: str) -> str:
    """
    Trigger function bound directly to the web interface submit button.
    Runs the OpenAI Agent SDK system asynchronously.
    """
    if not target_sector.strip():
        return "⚠️ Please provide a valid market category, sector, or business theme."
    
    prompt = f"Please run a comprehensive market analysis report on the following industry sector: {target_sector}"
    
    try:
        # Run the multi-agent orchestration
        result = await Runner.run(
        starting_agent=triage_agent, 
        input=prompt,
        max_turns=5 # Added safety cap to limit token usage!
    )
        return result.final_output
    except Exception as e:
        return f"❌ An orchestration error occurred inside the system layer:\n{str(e)}"

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
with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue", secondary_hue="slate")) as demo:
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
            
        with gr.Column(scale=2):
            output_markdown = gr.Markdown(
                label="Generated Intelligence Brief",
                value="*The compiled analyst document output will display here ONCE execution completes.*"
            )
            
    # Bind the submit event asynchronously 
    submit_btn.click(
        fn=analyze_market,
        inputs=input_box,
        outputs=output_markdown
    )

# Launch system block loop
if __name__ == "__main__":
    demo.queue().launch()