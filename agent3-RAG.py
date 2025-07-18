# ---------------- RAG-Based Chunk Retrieval ----------------
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

@tool
def retrieve_chunks(paper_json: list[dict], query: str) -> list[dict]:
    """
    Performs RAG-based retrieval:
    1. Splits full paper text into chunks.
    2. Embeds chunks and query.
    3. Returns top-5 most relevant chunks with paper IDs.
    """
    # Step 1: Collect all chunks with associated paper IDs
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    all_chunks = []
    for paper in paper_json:
        paper_id = paper["id"]
        paper_text = paper.get("full_text", paper.get("abstract", ""))  # fallback to abstract
        chunks = text_splitter.split_text(paper_text)
        for chunk in chunks:
            all_chunks.append({"chunk": chunk, "paper_id": paper_id})

    # Step 2: Create FAISS vector store
    texts = [chunk["chunk"] for chunk in all_chunks]
    metadata = [{"paper_id": chunk["paper_id"]} for chunk in all_chunks]
    embeddings = OpenAIEmbeddings()  # You can replace with free embedding models if needed
    vector_store = FAISS.from_texts(texts, embeddings, metadatas=metadata)

    # Step 3: Retrieve top-5 most relevant chunks
    results = vector_store.similarity_search(query, k=5)
    return [{"paper_id": r.metadata["paper_id"], "chunk": r.page_content} for r in results]

# Agent 3 (RAG-based)
agent3 = create_react_agent(
    model=ChatOpenAI(model="gpt-3.5-turbo"),
    tools=[retrieve_chunks],
    prompt="Retrieve the top-5 most relevant chunks using vector similarity search."
)
