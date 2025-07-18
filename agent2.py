from langchain.tools import tool
from langchain.chat_models import ChatOpenAI
from langgraph.prebuilt import create_react_agent
import requests
import json

# ---------------- Agent 2: PubMed fetch ----------------
@tool
def fetch_pubmed(keywords: str) -> list[dict]:
    """Fetch top 10 PubMed papers (title + abstract) and select top 5 with LLM."""
    # Step 1: Fetch top-10 IDs
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": keywords,
        "retmode": "json",
        "retmax": 10,
    }
    ids = requests.get(search_url, params=params).json()["esearchresult"]["idlist"]

    papers = []
    for pid in ids:
        # Step 2: Fetch details including abstract
        fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        fetch_params = {
            "db": "pubmed",
            "id": pid,
            "retmode": "xml",
        }
        xml_data = requests.get(fetch_url, params=fetch_params).text

        # Extract title and abstract from XML
        import xml.etree.ElementTree as ET
        root = ET.fromstring(xml_data)
        title = root.findtext(".//ArticleTitle", default="No Title")
        abstract = root.findtext(".//AbstractText", default="No Abstract")
        papers.append({"id": pid, "title": title, "abstract": abstract})

    # Step 3: Use LLM to select top 5
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    ranking_prompt = (
        f"Given the following 10 PubMed papers about '{keywords}', "
        "select the 5 most relevant ones based on their titles and abstracts:\n\n"
        + "\n".join(
            [f"{i+1}. {p['title']}\nAbstract: {p['abstract']}\n(PMID: {p['id']})"
             for i, p in enumerate(papers)]
        )
        + "\n\nReturn a JSON list of the 5 selected paper IDs."
    )

    response = llm.predict(ranking_prompt)
    try:
        selected_ids = json.loads(response)
    except json.JSONDecodeError:
        selected_ids = [p["id"] for p in papers[:5]]

    top5 = [p for p in papers if p["id"] in selected_ids]
    return top5


agent2 = create_react_agent(
    model=ChatOpenAI(model="gpt-3.5-turbo"),
    tools=[fetch_pubmed],
    prompt="Fetch 10 PubMed papers (with abstracts) and select the 5 most relevant."
)
