from dataclasses import dataclass
from enum import Enum

class LocalHref(Enum):
    Root        = 0
    Landing     = 1
    Product     = 2
    Contact     = 3
    Donate      = 4

@dataclass
class OutHref:
    to: str
