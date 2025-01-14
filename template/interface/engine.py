from template.interface.datapage import DataPage

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class TemplateConfig:
    debug: bool
    path: str

class TemplateEngine(ABC):
    @abstractmethod
    def Init(self, config: TemplateConfig) -> None:
        pass

    @abstractmethod
    def Run(self, datapage: DataPage) -> None:
        pass
