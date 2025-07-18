import requests
import json
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

# ---------------- Agent 3: RAG chunk retrieval with LLM ranking ----------------
@tool
def retrieve_chunks(paper_json: list[dict], user_query: str) -> list[dict]:
    """
    Retrieves the full text for each paper, splits into chunks,
    and uses the LLM to select the top-5 most relevant chunks.
    Returns a list of dictionaries with 'paper_id' and 'chunk'.
    """
    all_chunks = []

    # Step 1: Fetch and split texts
    for paper in paper_json:
        efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        efetch_params = {
            "db": "pubmed",
            "id": paper["id"],
            "retmode": "text",
            "rettype": "abstract"  # Use 'full' if full text is available
        }
        response = requests.get(efetch_url, params=efetch_params)
        full_text = response.text.strip()

        # Split text into 200-word chunks
        words = full_text.split()
        chunk_size = 200
        chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

        for c in chunks:
            all_chunks.append({"paper_id": paper["id"], "chunk": c})

    # Step 2: Ask LLM to rank chunks
    prompt = (
        f"You are an expert biomedical researcher. "
        f"Given the query: '{user_query}', select the 5 most relevant chunks from the list below. "
        f"Return a JSON list of objects with 'paper_id' and 'chunk'.\n\nChunks:\n"
    )

    for i, chunk in enumerate(all_chunks):
        prompt += f"{i + 1}. (Paper {chunk['paper_id']}) {chunk['chunk']}\n"

    ranking_response = llm.invoke([HumanMessage(content=prompt)])
    raw_output = ranking_response.content.strip()

    # Step 3: Attempt to parse JSON from LLM response
    try:
        top_chunks = json.loads(raw_output)
        if isinstance(top_chunks, list):
            return top_chunks
        else:
            raise ValueError("Parsed output is not a list.")
    except json.JSONDecodeError:
        # Fallback if the LLM doesn't return valid JSON
        print("Warning: Could not parse LLM output as JSON. Returning raw output.")
        return [{"paper_id": "unknown", "chunk": raw_output}]


agent3 = create_react_agent(
    model=llm,
    tools=[retrieve_chunks],
    prompt="From full texts, retrieve five key evidence chunks most relevant to the user question."
)
