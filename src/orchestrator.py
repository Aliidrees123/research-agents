import asyncio
from agents import Runner
from ai_agents.plan_agent import WebSearchItem, WebSearchPlan
from ai_agents.writer_agent import ReportData


class EssayOrchestrator:

    def __init__(self, plan_agent, search_agent, writer_agent, review_agent, edit_agent):
        self.plan_agent = plan_agent
        self.search_agent = search_agent
        self.writer_agent = writer_agent
        self.review_agent = review_agent
        self.edit_agent = edit_agent

    async def plan_queries(self, query: str) -> WebSearchPlan:
        result = await Runner.run(self.plan_agent, f'Query: {query}')
        return result.final_output_as(WebSearchPlan)
    
    async def conduct_searches(self, search_plan: WebSearchPlan) -> list[str]:
        tasks = [asyncio.create_task(self.search(item)) for item in search_plan.searches]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                results.append(result)
        return results
    
    async def search(self, item: WebSearchItem) -> str | None:
        prompt = f'Search term: {item.query}\nReason for searching: {item.reason}'
        try:
            result = await Runner.run(self.search_agent, prompt)
            result = str(result.final_output)
            return result
        except Exception:
            return None

    async def write_essay(self, query: str, search_results: list[str]) -> str:
        prompt = f'Original query: {query}\nSummarised search results: {search_results}'
        result = await Runner.run(self.writer_agent, prompt)
        return result.final_output

    async def review_essay(self, query: str, search_results: list[str], report: str) -> str:
        prompt = f'Original query: {query}\nSummarised search results: {search_results}\nEssay draft: {report}'
        result = await Runner.run(self.review_agent, prompt)
        return result.final_output
    
    async def edit_essay(self, report: ReportData, feedback: str) -> str:
        prompt = f'Report: {report}\nFeedback: {feedback}'
        result = await Runner.run(self.edit_agent, prompt)
        return result.final_output
    
    