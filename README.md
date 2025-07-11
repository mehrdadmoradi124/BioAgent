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
```

###  🔑 Set Your OpenAI API Key
You need an OpenAI API key to run this project. Choose one of the following options:

Option A – Set as environment variable (Recommended):
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

Option B – Set directly in main.py (Not recommended for production):
```bash
import os
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
```
### ▶️ Run the Agent Chain
Once your environment is set up and your API key is configured, you can run the main script:
```bash
python main.py
```
You will then be prompted to enter a biomedical question. For example:

What are treatments for glioblastoma resistant to temozolomide?

## ✅ Example Output
Here's a glimpse of the typical output you can expect when running the agent chain:

🧠 Extracted Keywords: glioblastoma, temozolomide, resistance
📄 Top 10 PubMed Papers fetched
📚 Selected 5 Relevant Chunks
✍️ Draft Answer:
“Glioblastoma resistant to temozolomide can be treated with…”
📎 Citations: [PMID:12345678], [PMID:98765432], …
✅ Final Answer (Refined): …

## 📌 Notes & Future Extensions
This pipeline is designed to be extensible and can be adapted to other biomedical domains and integrated with different Large Language Models.

For full offline deployment and greater control, consider replacing OpenAI with open-source models.

## 📖 License
This project is released under the MIT License. See the LICENSE file for more details.

