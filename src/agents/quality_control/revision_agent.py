from agents import Agent

INSTRUCTIONS = """
    You are a professor. You will be given an essay and some feedback on how to make it
    to publication standard. Implement the feedback and respond only with the finished
    essay."""

def build_revision_agent(config):
    revision_agent = Agent(
        name="RevisionAgent",
        instructions=INSTRUCTIONS,
        model=config.model
    )
    return revision_agent
