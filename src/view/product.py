from dataclasses import dataclass
from enum import Enum

@dataclass
class ProductCard:
    head: str
    body: str
    star: bool

class LevelFiltered(Enum):
    NotFiltered     = 0
    Major           = 1
    Toy             = 2
    Deprecated      = 3

@dataclass
class SeriesFiltered(Enum):
    NonFiltered     = 0
    Host            = 1
    Cod             = 2
    Etc             = 3

@dataclass
class StarFiltered(Enum):
    NonFiltered     = 0
    Star            = 1
    NonStar         = 2

@dataclass
class Filter:
    level: LevelFiltered
    series: SeriesFiltered
    star: StarFiltered

@dataclass
class ProductPage:
    filter: Filter
    cards: list[ProductCard]
