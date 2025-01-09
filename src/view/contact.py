from view.shared.href import OutHref

from enum import Enum

class Icon(Enum):
    Email       = 0
    PhoneCall   = 1

    LinkedIn    = 2
    Discord     = 3
    Facebook    = 4
    Twiiter     = 5

    Youtube     = 6
    Blog        = 7
    Github      = 8

class ContactCard:
    head: str
    href: OutHref
    icon: Icon

class ContactPage:
    contacts: list[ContactCard]
