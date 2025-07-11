🧠 Agent Workflow
	1.	Agent 1 – Keyword Extractor
➤ Extracts relevant biomedical keywords from the user’s question.
	2.	Agent 2 – PubMed Retriever
➤ Uses those keywords to fetch top 10 relevant papers from PubMed.
	3.	Agent 3 – Chunk Selector
➤ Applies RAG-style retrieval to select the 5 most relevant text chunks.
	4.	Agent 4 – Answer Generator
➤ Generates a concise, cited answer using the chunks and original question.
	5.	Agent 5 – Answer Refiner
➤ Improves the answer for clarity, completeness, and factual accuracy.

⸻

🗂️ File Structure

biomed-qa/
├── agent1.py         # Keyword extractor
├── agent2.py         # PubMed fetcher
├── agent3.py         # RAG chunk retriever
├── agent4.py         # Answer generator
├── agent5.py         # Self-critic and refiner
├── main.py           # Entry point to run the full pipeline
├── requirements.txt  # Required Python packages
└── README.md         # This file

⸻

🚀 How to Run
	1.	Create Environment

conda create -n biomed python=3.10
conda activate biomed
pip install -r requirements.txt
	2.	Set Your OpenAI API Key

Option A – set as environment variable:
export OPENAI_API_KEY=“your-openai-api-key”

Option B – set directly in main.py:

import os
os.environ[“OPENAI_API_KEY”] = “your-openai-api-key”
	3.	Run the Agent Chain

python main.py

You will be prompted to enter a biomedical question, e.g.:

What are treatments for glioblastoma resistant to temozolomide?

⸻

✅ Example Output

🧠 Extracted Keywords: glioblastoma, temozolomide, resistance
📄 Top 10 PubMed Papers fetched
📚 Selected 5 Relevant Chunks
✍️ Draft Answer:
“Glioblastoma resistant to temozolomide can be treated with…”
📎 Citations: [PMID:12345678], [PMID:98765432], …
✅ Final Answer (Refined): …

⸻

📌 Notes
	•	This pipeline can be extended to other biomedical domains and LLMs.
	•	Consider replacing OpenAI with open-source models for full offline deployment.

⸻

📖 License

MIT License. See LICENSE for details.
