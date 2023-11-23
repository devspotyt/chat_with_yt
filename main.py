from src.handlers.app import GradioApp
from src.settings import settings


def main():
    gradio_app = GradioApp(settings.config_path)
    app = gradio_app.build_ui()
    app.launch()


if __name__ == '__main__':
    main()
