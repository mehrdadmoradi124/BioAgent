# ---------------- Agent 3: RAG chunk retrieval ----------------
@tool
def retrieve_chunks(paper_json: list[dict]) -> list[str]:
    """Returns top-5 relevant chunks (mocked for now)."""
    chunks = []
    for paper in paper_json[:5]:
        chunks.append(f"Relevant finding from paper '{paper['title']}'")
    return chunks

agent3 = create_react_agent(
    model=ChatOpenAI(model="gpt-3.5-turbo"),
    tools=[retrieve_chunks],
    prompt="From abstracts, retrieve five key evidence chunks."
)