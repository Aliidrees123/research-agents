from agents import Agent, WebSearchTool, ModelSettings

INSTRUCTIONS = """"
    You are a research assistant, given a search term, you must search the web for that term and produce a concise summary
    of the results. THe summary must have 3-4 paragraphs and less than 500 words. Capture the main points. Write succintly,
    no need to have complete sentences or good grammar. This will be consumed by someone synthesising a report, so it is
    vital that you capture the essence and ignore any fluff. Do not include any additional commentary other than the summary
    itself."""

def build_search_agent(config):
    search_agent = Agent(
    name="SearchAgent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool(search_context_size="low")],
    model=config.model,
    model_settings=ModelSettings(tool_choice="required")
    )
    return search_agent
