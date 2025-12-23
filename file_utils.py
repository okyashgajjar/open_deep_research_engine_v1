from pypdf import PdfReader


def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    return ""


def summarize_file_text(text: str):
    # Safe lightweight summary (no LLM cost)
    return text[:1500]
