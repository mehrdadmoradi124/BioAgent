# ---------------- Agent 4: Answer generation with citations ----------------
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.tools import tool

llm = ChatOpenAI(model="gpt-3.5-turbo")

@tool
def rerank_chunks(question: str, chunks: list[str]) -> list[str]:
    """Uses LLM to rank chunks and return the top-3 most relevant ones."""
    prompt = PromptTemplate(
        input_variables=["question", "chunks"],
        template="""
You are given a question and a list of text chunks from papers. 
Rank the chunks based on their relevance to the question, and output the top 3.

Question: {question}
Chunks:
{chunks}

Return the top 3 chunks as a numbered list.
"""
    )
    formatted_prompt = prompt.format(question=question, chunks="\n".join(chunks))
    response = llm.predict(formatted_prompt)
    # Extract top 3 chunks (assuming response is a numbered list)
    top_chunks = response.split("\n")[:3]
    return [chunk.strip("123. ") for chunk in top_chunks if chunk.strip()]

agent4 = create_react_agent(
    model=llm,
    tools=[rerank_chunks],
    prompt="""
Using the user question and the top-3 ranked chunks (already provided by the tool), 
draft a concise answer with inline citations such as (Paper ID1, Paper ID2).
"""
)
