from agents import Agent

INSTRUCTIONS = """
    You are a professor. You will be given an essay and some feedback on how to make it
    to publication standard. Implement the feedback and respond only with the finished
    essay."""

def build_edit_agent(config):
    edit_agent = Agent(
        name="EditAgent",
        instructions=INSTRUCTIONS,
        model=config.model
    )
    return edit_agent
