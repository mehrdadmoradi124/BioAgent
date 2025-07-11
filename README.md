# 🔬 biomed-qa: A Biomedical Question Answering Agent

Welcome to biomed-qa, a robust question answering system designed to provide concise, cited answers to biomedical questions by leveraging the power of large language models (LLMs) and PubMed. This project implements a multi-agent pipeline for efficient information retrieval and synthesis.

---

## 🧠 Agent Workflow

This system operates through a carefully orchestrated chain of specialized agents, each contributing to the final, accurate answer.

1.  **Agent 1 – Keyword Extractor**
    * ➤ Extracts relevant biomedical keywords from the user’s question.

2.  **Agent 2 – PubMed Retriever**
    * ➤ Uses those keywords to fetch the top 10 relevant papers from PubMed.

3.  **Agent 3 – Chunk Selector**
    * ➤ Applies Retrieval-Augmented Generation (RAG)-style retrieval to select the 5 most relevant text chunks from the fetched papers.

4.  **Agent 4 – Answer Generator**
    * ➤ Generates a concise, cited answer using the selected chunks and the original user question.

5.  **Agent 5 – Answer Refiner**
    * ➤ Improves the answer for clarity, completeness, and factual accuracy through a self-criticism mechanism.

---

## 🚀 How to Run

Follow these simple steps to set up and run the biomed-qa agent chain on your local machine.

### ⚙️ Create Environment

It's highly recommended to use a `conda` environment for dependency management:

```bash
conda create -n biomed python=3.10
conda activate biomed
pip install -r requirements.txt
