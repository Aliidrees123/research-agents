from agents import Agent
from pydantic import BaseModel, Field

INSTRUCTIONS = """
    You are a senior academic editor and writing reviewer. You are given a completed essay along with its original query and any supporting research summaries.
    Your task is to evaluate the essay and provide structured, prioritized feedback to improve it to publication standard. Focus on clarity, structure, coherence,
    and adherence to the original query. Identify critical and minor issues, highlight strengths, and provide actionable improvement points. Do not 
    rewrite the essay or add new content. Only critique and guide revision."""

class Feedback(BaseModel):
    critical_issues: str = Field(description="Major problems that must be fixed to improve essay quality and correctness")
    minor_issues: str = Field(description="Smaller issues such as wording, clarity, or flow improvements that are optional to fix")
    strengths: str = Field(description="Key positive aspects of the essay including structure, arguments, and writing quality")
    top_actions: str = Field(description="Prioritised list of the most important changes needed to improve the essay")

def build_review_agent(config):
    review_agent = Agent(
        name="ReviewAgent",
        instructions=INSTRUCTIONS,
        model=config.model,
        output_type=Feedback
    )
    return review_agent