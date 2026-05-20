from agents import Agent

INSTRUCTIONS = """
    You are a professor. You will be given an essay and some feedback on how to improve it. Implement the
    feedback and respond only with the finished essay. Ensure the essay is in clean academic prose with no
    Markdown formatting, symbols, or styling elements, using only plain paragraphs and standard punctuation."""

def build_edit_agent(config):
    edit_agent = Agent(
        name="EditAgent",
        instructions=INSTRUCTIONS,
        model=config.model
    )
    return edit_agent
