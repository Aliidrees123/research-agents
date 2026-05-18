from agents import Agent

INSTRUCTIONS = """
    You are a senior academic editor and writing reviewer.
    You are given a completed essay on an arbitrary topic.
    Your task is to critically evaluate the essay and provide structured feedback to improve its quality to publication standard.
    Respond only with the feedback, nothing else"""

def build_review_agent(config):
    review_agent = Agent(
        name="ReviewAgent",
        instructions=INSTRUCTIONS,
        model=config.model
    )