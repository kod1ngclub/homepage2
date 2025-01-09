from enum import Enum

from model.series import SeriesName

class LevelName(Enum):
    Major       = 0
    Toy         = 1
    Deprecated  = 2

class Product:
    name: str
    description: str
    href: str

    level: LevelName
    series: SeriesName
    star: bool
