from agents import Agent

INSTRUCTIONS = """
    You are a senior academic editor and writing reviewer. You are given a completed essay along with its original query and any supporting research summaries.
    Your task is to evaluate the essay and provide structured, prioritized feedback to improve it to publication standard. Focus on clarity, structure, coherence,
    and adherence to the original query. Identify issues, highlight strengths, and provide actionable improvement points. Do not rewrite the essay or add new 
    content. Only critique and guide revision."""

def build_review_agent(config):
    review_agent = Agent(
        name="ReviewAgent",
        instructions=INSTRUCTIONS,
        model=config.model
    )
    return review_agent