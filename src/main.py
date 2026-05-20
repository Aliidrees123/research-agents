import asyncio

from config import Config
from agents import Runner

from ai_agents.plan_agent import build_plan_agent
from ai_agents.search_agent import build_search_agent
from ai_agents.writer_agent import build_writer_agent
from ai_agents.quality_control.review_agent import build_review_agent
from ai_agents.quality_control.edit_agent import build_edit_agent

from orchestrator import EssayOrchestrator


async def main():
    # load config
    config = Config.from_env()

    # build agents
    plan_agent = build_plan_agent(config)
    search_agent = build_search_agent(config)
    writer_agent = build_writer_agent(config)
    review_agent = build_review_agent(config)
    edit_agent = build_edit_agent(config)

    # build orchestrator
    orch = EssayOrchestrator(
        plan_agent=plan_agent,
        search_agent=search_agent,
        writer_agent=writer_agent,
        review_agent=review_agent,
        edit_agent=edit_agent
    )

    # test query
    query = "Explain the impact of artificial intelligence on healthcare"

    # run pipeline
    result = await orch.run_pipeline(query)

    print("\n\n===== FINAL ESSAY =====\n")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())