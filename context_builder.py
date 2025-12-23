# context_builder.py

def build_context(previous_summary=None, file_summary=None):
    context_parts = []

    if previous_summary:
        context_parts.append(
            f"Previously researched topics (do not repeat):\n{previous_summary}"
        )

    if file_summary:
        context_parts.append(
            f"User-provided document context:\n{file_summary}"
        )

    return "\n\n".join(context_parts)
