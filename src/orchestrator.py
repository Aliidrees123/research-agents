import asyncio
from agents import Runner
from ai_agents.plan_agent import WebSearchItem, WebSearchPlan
from ai_agents.quality_control.review_agent import Feedback


class EssayOrchestrator:

    def __init__(self, plan_agent, search_agent, writer_agent, review_agent, edit_agent):
        self.plan_agent = plan_agent
        self.search_agent = search_agent
        self.writer_agent = writer_agent
        self.review_agent = review_agent
        self.edit_agent = edit_agent

    async def run_pipeline(self, query):
        queries = await self.plan_queries(query)
        summarisations = await self.conduct_searches(queries)
        essay_draft = await self.write_essay(query, summarisations)
        essay_feedback = await self.review_essay(query, summarisations, essay_draft)
        final_essay = await self.edit_essay(essay_draft, essay_feedback)
        return final_essay

    async def plan_queries(self, query: str) -> WebSearchPlan:
        print("Planning queries")
        result = await Runner.run(self.plan_agent, f'Query: {query}')
        print("Queries planned")
        return result.final_output_as(WebSearchPlan)
    
    async def conduct_searches(self, search_plan: WebSearchPlan) -> list[str]:
        print("Creating tasks")
        tasks = [asyncio.create_task(self.search(item)) for item in search_plan.searches]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                results.append(result)
        print("Finalising summaries")
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
        print("Writing essay")
        prompt = f'Original query: {query}\nSummarised search results: {search_results}'
        result = await Runner.run(self.writer_agent, prompt)
        print("Essay written")
        return result.final_output

    async def review_essay(self, query: str, search_results: list[str], report: str) -> Feedback:
        print("Reviewing essay")
        prompt = f'Original query: {query}\nSummarised search results: {search_results}\nEssay draft: {report}'
        result = await Runner.run(self.review_agent, prompt)
        print("Essay reviewed")
        return result.final_output_as(Feedback)
    
    async def edit_essay(self, report: str, feedback: Feedback) -> str:
        print("Editing essay")
        prompt = f'Report: {report}\nFeedback: {feedback.model_dump()}'
        result = await Runner.run(self.edit_agent, prompt)
        print("Essay edited")
        return result.final_output
