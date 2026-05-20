import gradio as gr
import asyncio


def build_ui(orchestrator):
    def run_pipeline(query: str):
        return asyncio.run(orchestrator.run_pipeline(query))

    ui = gr.Interface(
        fn=run_pipeline,
        inputs=gr.Textbox(label="Enter your essay question"),
        outputs=gr.Textbox(label="Final Essay"),
        title="AI Essay Pipeline"
    )

    return ui