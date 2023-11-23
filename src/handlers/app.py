from typing import Dict
import gradio as gr
from src.handlers.yt_handler import YTHandler
from src.models.config import load_resolvers
from src.models.resolver import AIChatResolverBase


class GradioApp:
    def __init__(self, config_path):
        self.resolvers: Dict[str, AIChatResolverBase] = load_resolvers(
            file_path=config_path)
        self.current_resolver = None
        self.current_transcript = ""

    def process_video(self, url: str):
        """ Process the YouTube video and store the formatted transcript. """
        yt_handler = YTHandler(url)
        self.current_transcript = yt_handler.get_formatted_transcript()
        return "Video processed. You can start asking questions now."

    def chat_with_video(self, message, history):
        """ Use AI to answer video related questions based on transcript. """
        if not self.current_resolver:
            return "Please select an AI model first."
        combined_input = f"Context: {self.current_transcript}\nQuestion: {message}"
        response = self.current_resolver.query(
            [{"content": combined_input, "role": "user"}])
        history.append((message, response[0]))
        return "", history

    def build_ui(self):
        with gr.Blocks() as app:
            gr.Markdown("### YouTube Video Processor and Chat")
            gr.Markdown(
                "Enter a YouTube video URL and use the chatbox to ask questions about the video.")

            with gr.Row():
                video_url = gr.Textbox(label="YouTube Video URL")
                process_button = gr.Button("Process Video")
            process_output = gr.Text(label="Status")

            with gr.Row():
                resolver_dropdown = gr.Dropdown(list(self.resolvers.keys()),
                                                label="Choose AI Resolver")

            def update_resolver(resolver_name):
                self.current_resolver = self.resolvers[resolver_name]

            resolver_dropdown.change(update_resolver, resolver_dropdown)

            chatbot = gr.Chatbot(height=400)
            msg = gr.Textbox(placeholder="Enter your question here...",
                             container=False, scale=5)
            msg.submit(self.chat_with_video, inputs=[msg, chatbot],
                       outputs=[msg, chatbot])
            clear = gr.ClearButton([msg, chatbot])

            process_button.click(self.process_video, inputs=video_url,
                                 outputs=process_output)

        return app
