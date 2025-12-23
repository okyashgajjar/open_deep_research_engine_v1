# engine.py
import asyncio
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd=True))
DRY_RUN = True 

from storage import create_research, update_research
from context_builder import build_context
from cost_tracker import calculate_cost

from open_deep_research.deep_researcher import supervisor
from open_deep_research.configuration import (
    RunnableConfig,
    Configuration,
    SearchAPI,
)


def run_research_engine(
    query: str,
    parent_id: str | None = None,
    parent_summary: str | None = None,
    file_summary: str | None = None,
):
    research_id = create_research(query, parent_id=parent_id)

    context = build_context(
        previous_summary=parent_summary,
        file_summary=file_summary,
    )

    state = {
        "query": query,
        "notes": context,
        "messages": [],
    }

    # 🔑 RunnableConfig (runtime)
    runnable_config = RunnableConfig(
        recursion_limit=5,
        configurable={
            # ⬇️ THESE MAP DIRECTLY TO Configuration fields
            "research_model": "openai:gpt-3.5-turbo",
            "final_report_model": "openai:gpt-3.5-turbo",
            "compression_model": "openai:gpt-3.5-turbo",
            "summarization_model": "openai:gpt-3.5-turbo",

            "search_api": SearchAPI.NONE,  # 🚫 no web search
            "max_researcher_iterations": 2,
            "max_concurrent_research_units": 1,
        },
    )

    # Optional: inspect resolved config (VERY USEFUL)
    resolved_config = Configuration.from_runnable_config(runnable_config)

    if DRY_RUN:
    # 🧪 Mock result (no API calls)
        result = {
            "final_report": (
                "This is a mock deep research report on the impact of AI "
                "in healthcare diagnostics. AI is improving early disease "
                "detection, reducing diagnostic errors, and supporting "
                "clinical decision-making through imaging and data analysis."
            ),
            "sources": [
                "World Health Organization (WHO)",
                "FDA",
                "Nature Medicine"
            ],
            "input_tokens": 1200,
            "output_tokens": 1800,
            "trace_id": "mock-trace-id"
        }
    else:
        # 🚀 Real execution (requires OpenAI credits)
        result = asyncio.run(supervisor(state, runnable_config))


    report = result.get("final_report", "")
    summary = report[:800]

    reasoning = (
        "Research executed using a controlled LangGraph workflow with "
        "planning, analysis, and final synthesis."
    )

    tokens = {
        "input": result.get("input_tokens", 0),
        "output": result.get("output_tokens", 0),
    }

    cost = calculate_cost(
        model="gpt-3.5-turbo",
        input_tokens=tokens["input"],
        output_tokens=tokens["output"],
    )

    update_research(
        research_id,
        status="COMPLETED",
        report=report,
        summary=summary,
        reasoning=reasoning,
        sources=result.get("sources", []),
        tokens=tokens,
        cost=cost,
        trace_id=result.get("trace_id"),
    )

    return research_id
