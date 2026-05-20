import asyncio

from config import Config
from orchestrator import EssayOrchestrator

from ai_agents.plan_agent import build_plan_agent
from ai_agents.search_agent import build_search_agent
from ai_agents.writer_agent import build_writer_agent
from ai_agents.quality_control.review_agent import build_review_agent
from ai_agents.quality_control.edit_agent import build_edit_agent

from ui import build_ui


def main():
    config = Config.from_env()

    orch = EssayOrchestrator(
        build_plan_agent(config),
        build_search_agent(config),
        build_writer_agent(config),
        build_review_agent(config),
        build_edit_agent(config),
    )

    ui = build_ui(orch)
    ui.launch()


if __name__ == "__main__":
    main()