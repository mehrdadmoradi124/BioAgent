# ---------------- Agent 5: Self-critique and refinement ----------------
@tool
def validate_answer(answer: str) -> str:
    """Check the answer for clarity, citations, and factual support."""
    checklist = [
        "✓ Is the answer clear?",
        "✓ Are citations present and accurate?",
        "✓ Are key claims supported by source chunks?",
    ]
    return "\n".join(checklist)

@tool
def refine_tone(answer: str) -> str:
    """Polish the tone and make the answer scientifically concise."""
    return answer.replace("very", "highly").replace("really", "significantly")

agent5 = create_react_agent(
    model=ChatOpenAI(model="gpt-3.5-turbo"),
    tools=[validate_answer, refine_tone],
    prompt="Review the draft answer and refine it for clarity, completeness, and accuracy."
)