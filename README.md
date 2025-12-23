# 🔬 Deep Research Engine

AI-Powered Research with History, Continuation & File Context

---

## 📌 Overview

This project is a Deep Research Engine that performs multi-step AI-powered research, keeps research history, allows continuation of past research, supports file uploads as context, and tracks cost & tokens.

The system is built by wrapping an existing open-source research agent instead of rewriting it, following real-world engineering practices.

> ⚠️ Core research logic is NOT rewritten.  
> All extensions are built around the existing workflow.

---

## 🎯 Key Features

- ✅ Deep multi-step AI research  
- ✅ Research history persistence  
- ✅ Research continuation (parent → child)  
- ✅ PDF / TXT file upload as context  
- ✅ High-level reasoning visibility  
- ✅ Token & cost tracking  
- ✅ Dry-run mode (no API cost)  
- ✅ Streamlit UI (easy to demo)

---

## 🧠 High-Level Architecture

User (Browser)  
   ↓  
Streamlit UI (`app.py`)  
   ↓  
Research Engine (`engine.py`)  
   ↓  
Open Deep Research Agent (LangGraph)  
   ↓  
Storage Layer (in-memory DB)

---

## 📁 Project Structure

```
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
```

---

## 🔧 Technology Stack

Layer | Technology
--- | ---
UI | Streamlit
Backend Logic | Python
AI Framework | LangChain + LangGraph
Research Agent | langchain-ai/open_deep_research
Tracing | LangSmith (optional)
Storage | In-memory (can be replaced with DB)

---

## 🧩 How the System Works

### 1️⃣ Research Execution

When a user enters a research query:

- Streamlit sends the query to `engine.py`
- The engine prepares the initial research state
- The existing LangGraph workflow performs:
  - Planning
  - Research
  - Reflection
  - Final synthesis
- A structured research report is returned

> 📌 Important: The core research workflow is not modified.

---

### 2️⃣ Research History

Each research session is stored with:

- Research ID  
- Original query  
- Final report  
- Summary  
- Token usage & cost  
- Parent research ID (if continued)

This enables:

- Viewing previous research  
- Reusing past work  
- Building research chains

---

### 3️⃣ Research Continuation (Parent → Child)

Continuation allows users to extend previous research.

Flow:

1. User selects an existing research
2. Previous summary is injected into the new research context
3. The agent avoids repeating already covered topics
4. Parent → child relationship is preserved

Example:

- Research 1: AI in healthcare diagnostics  
- Research 2: Ethical and regulatory challenges

---

### 4️⃣ File Upload as Context (PDF / TXT)

Users can upload PDF or TXT files to guide research.

Flow:

1. File is uploaded via Streamlit
2. Text is extracted
3. A short summary is created
4. Summary is injected into research context

> 📌 Uploaded files act as trusted user-provided sources.

---

### 5️⃣ Reasoning Visibility (Safe)

The system stores high-level reasoning, such as:

- Research planning steps  
- Source selection logic  
- Synthesis explanation

- ❌ Raw chain-of-thought is NOT exposed  
- ✅ Only summarized reasoning is shown

---

### 6️⃣ Cost & Token Tracking

For each research run:

- Input tokens  
- Output tokens  
- Estimated cost

This helps users:

- Understand AI usage  
- Control expenses  
- Compare different research runs

---

### 7️⃣ Dry-Run Mode (No API Cost)

To avoid dependency on API credits, the engine supports:

```env
DRY_RUN=True
```

In this mode:

- No external API calls are made  
- Mock research output is generated  
- Full system behavior is demonstrated

> 📌 Ideal for take-home assignments and demos.

---

## 🖥️ Streamlit UI (`app.py`)

The UI provides:

- Research input box  
- File upload (PDF / TXT)  
- Research history sidebar  
- Continuation selection  
- Research report display  
- Token & cost details

> 📌 The UI layer contains no research logic.

---

## ⚙️ Environment Setup

1️⃣ Install dependencies

```
From inside the repo:

```bash
cd open_deep_research
pip install -e .

```

### What this does

- Registers `open_deep_research` as a Python package
- Adds it to PYTHONPATH
- Allows clean imports

🧠 Real life:

You told Python: *“This is a real library, trust it.”*

2️⃣ Create `.env` file (project root)

```env
OPENAI_API_KEY=your_openai_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=deep-research-engine
```

▶️ Run the Application

```bash
streamlit run app.py
```

Open in browser: http://localhost:8501

---

## 🔍 Design Decisions & Trade-offs

- Why Streamlit first?
  - Faster prototyping
  - Easy to demonstrate
  - UI separated from logic
  - Simple migration to Django later

- Why wrap instead of rewrite?
  - Follows project constraints
  - Respects open-source design
  - Reduces risk and complexity

- Why dry-run mode?
  - Avoids API quota issues
  - Makes evaluation easy
  - Keeps architecture intact

---

## 🔄 Future Improvements

- Replace in-memory storage with PostgreSQL  
- Add user authentication  
- Visualize research lineage (tree view)  
- Export reports (PDF / Markdown)  
- Migrate to Django + REST APIs  
- Background execution using Celery

---
## ✅ Conclusion

This project demonstrates how to build a persistent, extensible, and cost-aware deep research system using modern AI tooling without rewriting complex research logic.

It is internship-ready, interview-friendly, and scalable.