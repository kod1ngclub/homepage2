from template.interface import TemplateEngine

from view.app import App

class TestTemplateEngine(TemplateEngine):
    def Run(self, data: App) -> None:
        print("Tada! We did something! (maybe...)")
