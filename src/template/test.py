from template.interface.engine import TemplateEngine
from template.interface.datapage import DataPage

class TestTemplateEngine(TemplateEngine):
    def Run(self, datapage: DataPage) -> None:
        print("I think we did something!")
