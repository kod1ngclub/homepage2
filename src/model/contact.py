from enum import Enum

class Media(Enum):
    Email       = 0
    PhoneCall   = 1

    LinkedIn    = 2
    Discord     = 3
    Facebook    = 4
    Twiiter     = 5

    Youtube     = 6
    Blog        = 7
    Github      = 8

class Contact:
    name: str
    media: Media
    href: str
