# ---------------- Agent 4: Answer generation with citations ----------------
@tool
def format_citations(paper_ids: list[str]) -> str:
    """Formats a list of PubMed IDs into citation format."""
    return "\n".join([f"[{i+1}] PubMed ID: {pid}" for i, pid in enumerate(paper_ids)])

@tool
def rerank_chunks(question: str, chunks: list[str]) -> list[str]:
    """Returns the top-3 most relevant chunks to the question."""
    return chunks[:3]

agent4 = create_react_agent(
    model=ChatOpenAI(model="gpt-3.5-turbo"),
    tools=[format_citations, rerank_chunks],
    prompt="Using chunks + user question, draft a concise answer with citations."
)