from model.series import SeriesName

from dataclasses import dataclass
from enum import Enum

class LevelName(Enum):
    Major       = 0
    Toy         = 1
    Deprecated  = 2

@dataclass
class Product:
    name: str               = ""
    description: str        = ""
    href: str               = ""

    level: LevelName        = LevelName.Deprecated
    series: SeriesName      = SeriesName.Etc
    star: bool              = False
