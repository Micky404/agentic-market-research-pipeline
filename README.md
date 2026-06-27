
## 🏢 Multi-Agent Market Intelligence Hub

A production-ready, autonomous multi-agent orchestration pipeline built with the **OpenAI Agents SDK** and **Gradio**. This application automates complex market research operations by distributing tasks across a cooperative network of four specialized, state-aware AI specialists.

🚀 **Live Deployment:** [View Live App on Hugging Face Spaces](https://huggingface.co/spaces/mikapreci/multi-agent-intelligence-hub-by-Mickael-Precigout) 

---

## 🛠️ System Architecture & Workflow

The platform shifts away from brittle, monolithic prompts toward an asynchronous **Choreographed Mesh Network** where individual agents act as microservices with isolated concerns and native JSON context handoffs.

```text

[User Input]
│
▼
┌────────────────────────────────────────────────────────┐
│ 1. Triage Orchestrator (gpt-5.4-mini)                  │ ──► Logs routing intent
└────────────────────────────────────────────────────────┘
│ (JSON Context Handoff)
▼
┌────────────────────────────────────────────────────────┐
│ 2. Web Researcher (gpt-5.4-mini)                      │ ──► Triggers `web_search_scraper` tool
└────────────────────────────────────────────────────────┘
│ (Asynchronous Raw Data Payload)
▼
┌────────────────────────────────────────────────────────┐
│ 3. Trend Analyst (gpt-5.5)                             │ ──► Heavy reasoning & signal extraction
└────────────────────────────────────────────────────────┘
│ (Structured Trends Payload)
▼
┌────────────────────────────────────────────────────────┐
│ 4. Executive Writer (gpt-5.5)                          │ ──► Generates pristine Markdown asset
└────────────────────────────────────────────────────────┘
│
▼
[Gradio Modern Dashboard UI]

```

### 👥 The Agent Roster

1. **Triage Orchestrator (`gpt-5.4-mini`)**: Analyzes intent, maps out the macro downstream execution route, and logs state transitions before passing control.
2. **Web Researcher (`gpt-5.4-mini`)**: Interacts with the data layer via dedicated python function tools to scrape and ingest unstructured industry web data.
3. **Trend Analyst (`gpt-5.5`)**: Consumes the raw unstructured web context to extract structural shifts, macro tailwinds, and quantitative market signals.
4. **Executive Writer (`gpt-5.5`)**: Synthesizes the finalized analytical data points into a beautifully formatted Markdown Research Brief optimized for executive distribution.

---

## 💡 Key Engineering Highlights

* **Asymmetric Cost/Model Optimization**: Implements professional budget guardrails. Fast routing and scraping routines run on the highly performant `gpt-5.4-mini` tier, while maximum reasoning tokens are preserved exclusively for `gpt-5.5` reasoning layers during synthesis.
* **Deterministic Logging Tool Interceptors**: Overcomes the "black-box" execution constraint of `Runner.run()` by attaching custom `@function_tool` decorators. This allows autonomous agents to safely stream state updates back into local python global memories *while* a background orchestration is executing.
* **Algorithmic Edge-Case Controls**: Protects API token budgets by implementing a strict `max_turns=12` safety cap, preventing recursive loop degradation during complex multi-stage agent handoffs.
* **Modern UI Layout Design**: Styled using Gradio’s `Soft` thematic elements with fully isolated multi-column responsive containers, giving users a clear window into individual workspace loops.

---

## 📦 Local Installation & Setup

Ensure you have Python 3.11+ installed on your system.

### 1. Clone the Workspace
```bash
git clone [https://github.com/Micky404/agentic-market-research-pipeline.git](https://github.com/Micky404/agentic-market-research-pipeline.git)
cd agentic-market-research-pipeline

```

### 2. Configure Environment Variables

Create a secure `.env` file in the root directory:

```text
OPENAI_API_KEY=your_secret_openai_key
TAVILY_API_KEY=your_secret_tavily_search_key

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Boot Up the Dashboard

```bash
python app.py

```

Open `http://127.0.0.1:7860` in your browser to inspect the application.

---

## 🚀 Cloud Deployment Framework

This application is fully containerized and hosted natively using **Hugging Face Spaces**.

* Dependencies are dynamically compiled and verified using continuous integration via Gradio's server runtime.
* Secrets and API authentication bindings are managed directly through isolated, non-exposed environment injection keys.

---

### 👤 Developed By

* **Mickaël PRECIGOUT**
* Optimized for Enterprise Model Scaling, Token Cost Management, and Dynamic State Tracking.

```
