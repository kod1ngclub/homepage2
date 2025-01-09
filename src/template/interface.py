from view.app import App

from abc import ABC, abstractmethod

class TemplateEngine(ABC):
    @abstractmethod
    def Run(self, data: App) -> None:
        pass
