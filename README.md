---
title: "biomed-qa: A Biomedical Question Answering Agent"
author: "Your Name/Organization (Optional)"
date: "`r Sys.Date()`"
output:
  github_document:
    toc: true
    toc_depth: 2
---

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# 🔬 biomed-qa: A Biomedical Question Answering Agent

Welcome to `biomed-qa`, a robust question answering system designed to provide concise, cited answers to biomedical questions by leveraging the power of large language models (LLMs) and PubMed. This project implements a multi-agent pipeline for efficient information retrieval and synthesis.

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

## 🗂️ File Structure

The project is organized into a clear and intuitive directory structure:

biomed-qa/
├── agent1.py         # Keyword extractor
├── agent2.py         # PubMed fetcher
├── agent3.py         # RAG chunk retriever
├── agent4.py         # Answer generator
├── agent5.py         # Self-critic and refiner
├── main.py           # Entry point to run the full pipeline
├── requirements.txt  # Required Python packages
└── README.md         # This file (generated from README.Rmd)



