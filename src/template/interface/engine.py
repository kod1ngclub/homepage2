from template.interface.datapage import DataPage

from abc import ABC, abstractmethod

class TemplateEngine(ABC):
    @abstractmethod
    def Run(self, datapage: DataPage) -> None:
        pass
