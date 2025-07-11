# ---------------- Agent 2: PubMed fetch ----------------
@tool
def fetch_pubmed(keywords: str) -> list[str]:
    """Returns top-10 PubMed IDs and abstracts using E-utilities."""
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": keywords,
        "retmode": "json",
        "retmax": 10,
    }
    ids = requests.get(url, params=params).json()["esearchresult"]["idlist"]

    summaries = []
    for pid in ids:
        summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        sum_params = {
            "db": "pubmed",
            "id": pid,
            "retmode": "json",
        }
        summary = requests.get(summary_url, params=sum_params).json()
        title = summary["result"][pid]["title"]
        summaries.append({"id": pid, "title": title})
    return summaries

agent2 = create_react_agent(
    model=ChatOpenAI(model="gpt-3.5-turbo"),
    tools=[fetch_pubmed],
    prompt="Use keywords to fetch top-10 PubMed papers."
)