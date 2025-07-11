from agents.agent1 import agent as agent1
from agents.agent2 import agent as agent2
from agents.agent3 import agent as agent3
from agents.agent4 import agent as agent4
from agents.agent5 import agent as agent5
import os
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
def run_pipeline(user_prompt):
    print("\n🔍 Extracting keywords...")
    result1 = agent1.invoke({"messages": [{"role": "user", "content": user_prompt}]})
    keywords = result1.content
    print(f"🧠 Keywords: {keywords}")

    print("\n📚 Fetching PubMed papers...")
    result2 = agent2.invoke({"messages": [{"role": "user", "content": keywords}]})
    paper_data = result2.content
    print(f"📄 Papers fetched.")

    print("\n📑 Retrieving relevant chunks...")
    result3 = agent3.invoke({"messages": [{"role": "user", "content": paper_data}]})
    chunks = result3.content
    print(f"📌 Chunks:\n{chunks}")

    print("\n✏️ Generating initial answer with citations...")
    result4 = agent4.invoke({"messages": [
        {"role": "user", "content": user_prompt},
        {"role": "system", "content": f"Use the following evidence chunks:\n{chunks}"}
    ]})
    draft_answer = result4.content
    print(f"\n📋 Draft Answer:\n{draft_answer}")

    print("\n🧐 Refining answer...")
    result5 = agent5.invoke({"messages": [
        {"role": "user", "content": f"Please refine this answer:\n{draft_answer}"}
    ]})
    final_answer = result5.content

    print("\n✅ Final Answer:")
    print(final_answer)

if __name__ == "__main__":
    user_prompt = input("💬 Enter your biomedical question: ")
    run_pipeline(user_prompt)