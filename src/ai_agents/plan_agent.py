from pydantic import BaseModel, Field
from agents import Agent

SEARCHES = 3

INSTRUCTIONS = f"You are a helpful research assistant. Given a query, come up with a set of web searches to perform to best answer the query. Output {SEARCHES} terms to query for."

class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning as to why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answr the query.")

def build_plan_agent(config):
    plan_agent = Agent(
        name="PlanAgent",
        instructions=INSTRUCTIONS,
        model=config.model,
        output_type=WebSearchPlan
    )
    return plan_agent