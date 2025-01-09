from enum import Enum

class LocalHref(Enum):
    Landing     = 0
    Product     = 1
    Contact     = 2
    Doante      = 3

class OutHref:
    to: str
