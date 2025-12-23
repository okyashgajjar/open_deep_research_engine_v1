import streamlit as st

from engine import run_research_engine
from storage import get_research, list_research
from file_utils import extract_text_from_file, summarize_file_text

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Deep Research Engine",
    layout="wide"
)

st.title("🔬 Deep Research Engine")
st.caption("Deep AI-powered research with history, continuation & file context")

# -------------------------------------------------
# Sidebar: Research History & Continuation
# -------------------------------------------------
st.sidebar.header("📜 Research History")

history = list_research()

parent_id = None

if history:
    history_map = {
        r["id"]: r["query"]
        for r in history
    }

    parent_id = st.sidebar.selectbox(
        "Continue from previous research (optional)",
        options=[""] + list(history_map.keys()),
        format_func=lambda x: "None (Start fresh)" if x == "" else history_map[x][:40] + "..."
    )
else:
    st.sidebar.info("No previous research yet")

# -------------------------------------------------
# Main Section: New Research
# -------------------------------------------------
st.subheader("🧠 Start / Continue Research")

query = st.text_area(
    "Enter your research question",
    placeholder="Impact of AI on healthcare diagnostics",
    height=100
)

uploaded_file = st.file_uploader(
    "Upload context file (PDF or TXT)",
    type=["pdf", "txt"]
)

run_btn = st.button("🚀 Run Research")

# -------------------------------------------------
# Run Research Logic
# -------------------------------------------------
if run_btn and query.strip():

    file_summary = None
    parent_summary = None

    # ---- File Context ----
    if uploaded_file:
        with st.spinner("Reading uploaded file..."):
            file_text = extract_text_from_file(uploaded_file)
            file_summary = summarize_file_text(file_text)

    # ---- Continuation Context ----
    if parent_id:
        parent_research = get_research(parent_id)
        parent_summary = parent_research["summary"]

    with st.spinner("Running deep research..."):
        research_id = run_research_engine(
            query=query,
            parent_id=parent_id or None,
            parent_summary=parent_summary,
            file_summary=file_summary
        )

    st.success("Research completed successfully ✅")
    st.session_state["active_research_id"] = research_id

# -------------------------------------------------
# Select Which Research to Display
# -------------------------------------------------
result = None

if "active_research_id" in st.session_state:
    result = get_research(st.session_state["active_research_id"])
elif parent_id:
    result = get_research(parent_id)

# -------------------------------------------------
# Display Research Output
# -------------------------------------------------
if result:
    st.divider()
    st.subheader("📄 Research Report")

    st.markdown(result["report"])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📝 Summary")
        st.write(result["summary"])

        if result.get("parent_id"):
            st.caption(f"Continued from research ID: {result['parent_id']}")

    with col2:
        st.subheader("💰 Cost & Tokens")
        st.write(f"Input Tokens: {result['tokens'].get('input', 0)}")
        st.write(f"Output Tokens: {result['tokens'].get('output', 0)}")
        st.write(f"Estimated Cost: ${result['cost']}")

    st.divider()
    st.subheader("🔗 Sources")

    if result["sources"]:
        for src in result["sources"]:
            st.write(f"- {src}")
    else:
        st.write("No sources available")

    if result.get("trace_id"):
        st.info(f"LangSmith Trace ID: {result['trace_id']}")
