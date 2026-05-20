# Research Agents

A multi-agent research and writing application that turns a single topic into a researched long-form essay through a staged AI pipeline.

## What This Project Does

This project orchestrates five specialized AI agents to:

1. Plan search queries from a user topic.
2. Run web research and summarize findings.
3. Draft a long-form essay.
4. Review the draft with structured editorial feedback.
5. Edit the essay into a polished final version.

A Gradio interface exposes this workflow in a simple UI where users enter a topic and receive progressive status updates and final output.

## Core Architecture

- `PlanAgent`: creates a structured web-search plan (`WebSearchPlan`) with exactly 3 targeted searches.
- `SearchAgent`: performs web search (via `WebSearchTool`) and returns concise synthesis summaries.
- `WriterAgent`: generates a detailed markdown essay from topic + research summaries.
- `ReviewAgent`: evaluates draft quality and returns typed feedback (`critical_issues`, `minor_issues`, `strengths`, `top_actions`).
- `EditAgent`: applies feedback and outputs the final cleaned essay.
- `EssayOrchestrator`: coordinates all stages, including concurrent search execution with `asyncio`.

## Tech Stack

- Python 3.12+
- OpenAI Agents SDK (`openai-agents`)
- OpenAI API (`openai`)
- Gradio UI
- Pydantic models for structured agent outputs
- `python-dotenv` for configuration loading

## Project Structure

- `src/main.py` - app entrypoint and dependency wiring
- `src/config.py` - environment-based runtime config
- `src/orchestrator.py` - pipeline orchestration logic
- `src/ui.py` - Gradio interface + staged user feedback
- `src/ai_agents/` - specialized agent definitions
- `src/ai_agents/quality_control/` - review/edit quality loop

## Setup

1. Create and activate a Python 3.12+ virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env`:

```env
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4.1-mini
```

## Run

```bash
python src/main.py
```

Then open the Gradio app in your browser, enter an essay topic, and run the pipeline.

## Why This Is Interesting

This repo demonstrates practical multi-agent system design:

- Role-specialized agents instead of a single monolithic prompt.
- Typed intermediate outputs to improve reliability.
- Asynchronous fan-out/fan-in research stage.
- Iterative quality control with explicit review and revision phases.
- A lightweight product surface (UI) over advanced orchestration.
