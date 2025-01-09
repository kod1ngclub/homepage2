from enum import Enum

class LocalHref(Enum):
    ROOT        = 0
    Landing     = 1
    Product     = 2
    Contact     = 3
    Doante      = 4

class OutHref:
    to: str
