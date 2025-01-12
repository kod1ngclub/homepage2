from dataclasses import dataclass
from enum import Enum

class SeriesName(Enum):
    Host        = 0
    Cod         = 1
    Etc         = 2

@dataclass
class Series:
    name: SeriesName
    description: str
