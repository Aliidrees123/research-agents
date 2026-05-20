import gradio as gr
import asyncio


def build_ui(orchestrator):

    def run_pipeline(query: str):
        # Stage 1
        yield "Planning queries..."

        queries = asyncio.run(orchestrator.plan_queries(query))

        # Stage 2
        yield "Researching..."

        summaries = asyncio.run(orchestrator.conduct_searches(queries))

        # Stage 3
        yield "Writing essay..."

        essay = asyncio.run(orchestrator.write_essay(query, summaries))

        # Stage 4
        yield "Reviewing essay..."

        feedback = asyncio.run(orchestrator.review_essay(query, summaries, essay))

        # Stage 5
        yield "Editing essay..."

        final_essay = asyncio.run(orchestrator.edit_essay(essay, feedback))

        # Final output
        yield final_essay


    ui = gr.Interface(
        fn=run_pipeline,
        inputs=gr.Textbox(label="Essay Topic"),
        outputs=gr.Textbox(label="Generated Essay", lines=30, max_lines=50),
        title="AI Assisted Research Project",
        live=False,
        flagging_mode="never"
    )

    return ui