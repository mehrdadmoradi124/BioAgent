# Biomedical Question Answering with LangGraph Agents

This project implements a multi-agent biomedical question answering pipeline using [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://www.langchain.com/). It extracts keywords from a biomedical question, retrieves relevant PubMed papers, selects important evidence chunks, generates an answer with citations, and refines it.

---

## 🧠 Agent Workflow

1. **Agent 1 – Keyword Extractor**  
   Extracts relevant biomedical keywords from the user’s question.

2. **Agent 2 – PubMed Retriever**  
   Uses those keywords to fetch top 10 relevant papers from PubMed.

3. **Agent 3 – Chunk Selector**  
   Applies RAG-style retrieval to select the 5 most relevant text chunks.

4. **Agent 4 – Answer Generator**  
   Generates a concise, cited answer using the chunks and original question.

5. **Agent 5 – Answer Refiner**  
   Improves the answer for clarity, completeness, and accuracy.

---

## 🗂️ File Structure
biomed-qa/
│

│── agent1.py       # Keyword extractor
│── agent2.py       # PubMed fetcher
│── agent3.py       # RAG chunk retriever
│-─ agent4.py       # Answer generator
│── agent5.py       # Self-critic and refiner
│
├── main.py             # Entry point for running the full pipeline
├── README.md           # This file





---

## 🚀 How to Run

### 1. Create Environment

```bash
conda create -n biomed python=3.10
conda activate biomed
pip install -r requirements.txt




🧠 Extracted Keywords: glioblastoma, temozolomide, resistance
📄 Top 10 PubMed Papers fetched
📚 Selected 5 Relevant Chunks
✍️ Draft Answer:
    "Glioblastoma resistant to temozolomide can be treated with..."
📎 Citations: [PMID:12345678], [PMID:98765432], ...
✅ Final Answer (Refined): ...
