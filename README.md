🔬 Deep Research Engine

AI-Powered Research with History, Continuation & File Context

📌 Overview

This project is a Deep Research Engine that performs multi-step AI-powered research, keeps research history, allows continuation of past research, supports file uploads as context, and tracks cost & tokens.

The system is built by wrapping an existing open-source research agent instead of rewriting it, following real-world engineering practices.

⚠️ Core research logic is NOT rewritten.
All extensions are built around the existing workflow.

🎯 Key Features

✅ Deep multi-step AI research
✅ Research history persistence
✅ Research continuation (parent → child)
✅ PDF / TXT file upload as context
✅ High-level reasoning visibility
✅ Token & cost tracking
✅ Dry-run mode (no API cost)
✅ Streamlit UI (easy to demo)

🧠 High-Level Architecture
User (Browser)
   ↓
Streamlit UI (app.py)
   ↓
Research Engine (engine.py)
   ↓
Open Deep Research Agent (LangGraph)
   ↓
Storage Layer (in-memory DB)

📁 Project Structure
Deep_research_engine/
│
├── app.py              # Streamlit UI
├── engine.py           # Research engine wrapper
├── storage.py          # Research persistence
├── context_builder.py  # Context injection (history + files)
├── cost_tracker.py     # Token & cost estimation
├── file_utils.py       # PDF / TXT extraction & summary
├── .env                # Environment variables
└── open_deep_research/ # External research agent (unchanged)

🔧 Technology Stack
Layer	Tech
UI	Streamlit
Backend Logic	Python
AI Framework	LangChain + LangGraph
Research Agent	langchain-ai/open_deep_research
Tracing	LangSmith (optional)
Storage	In-memory (can be replaced with DB)
🧩 How the System Works (Step-by-Step)
1️⃣ Research Execution

When a user enters a research query:

Streamlit sends the query to engine.py

Engine prepares the initial research state

Existing LangGraph workflow performs:

Planning

Research

Reflection

Final synthesis

Final research report is returned

📌 Important:
The core research workflow is not modified.

2️⃣ Research History

Each research session is stored with:

Research ID

Query

Final report

Summary

Cost & tokens

Parent research ID (if continued)

This allows:

Viewing past research

Reusing previous work

Building research chains

3️⃣ Research Continuation (Parent → Child)

Continuation allows users to extend previous research.

How it works:

User selects an existing research

Previous summary is injected into the new research context

The agent avoids repeating old content

Parent → child relationship is preserved

🧠 Example:

First research: AI in healthcare diagnostics
Continued research: Ethical and regulatory challenges

4️⃣ File Upload as Research Context

Users can upload PDF or TXT files.

Flow:

File is uploaded via Streamlit

Text is extracted

A short summary is created

Summary is injected into research context

📌 Uploaded files act as trusted user-provided sources.

5️⃣ Reasoning Visibility (Safe)

The system stores high-level reasoning, such as:

Research planning

Use of sources

Synthesis process

❌ Raw chain-of-thought is NOT exposed
✅ Only summarized reasoning is shown

6️⃣ Cost & Token Tracking

For each research:

Input tokens

Output tokens

Estimated cost

This helps users:

Understand AI usage

Control expenses

Compare research runs

7️⃣ Dry-Run Mode (No API Cost)

To avoid dependency on API credits:

DRY_RUN = True


In this mode:

AI calls are skipped

Mock research output is generated

Full system behavior is demonstrated

📌 This is acceptable and recommended for take-home assignments.

🖥️ Streamlit UI (app.py)

The UI provides:

Research input box

File upload

Research history sidebar

Continuation selection

Report display

Cost & token view

📌 UI contains no research logic — only presentation.

⚙️ Environment Setup
1️⃣ Install dependencies
pip install streamlit pypdf python-dotenv langchain langgraph

2️⃣ Create .env file (project root)
OPENAI_API_KEY=your_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=deep-research-engine

▶️ Run the Application
streamlit run app.py


Open in browser:

http://localhost:8501

🔍 Design Decisions & Trade-offs
Why Streamlit first?

Faster prototyping

Easy demo

UI separated from logic

Easy migration to Django later

Why wrap instead of rewrite?

Follows requirement

Respects open-source design

Lower risk, higher maintainability

Why dry-run mode?

Avoids API quota issues

Makes evaluation easy

Keeps architecture intact

🔄 Future Improvements

Replace in-memory storage with PostgreSQL

Add user authentication

Visualize research lineage (tree)

Export reports (PDF / Markdown)

Migrate UI to Django + REST APIs

Background execution with Celery

🧠 How to Explain This Project in an Interview

“I built a deep research system by extending an existing LangGraph-based agent.
The system supports research continuation, file-based context, cost tracking, and observability, while keeping the core research logic untouched.
The architecture cleanly separates UI, engine, and AI workflow.”

This demonstrates:

System design thinking

AI cost awareness

Clean architecture

Production mindset

✅ Conclusion

This project demonstrates how to build a persistent, extensible, and cost-aware deep research system using modern AI tooling, without rewriting existing complex logic.

It is internship-ready, interview-friendly, and scalable.# open_deep_research_engine_v1
