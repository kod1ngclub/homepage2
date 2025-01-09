from view.shared.href import LocalHref
from view.shared.href import OutHref

from dataclasses import dataclass

@dataclass
class Button:
    text: str
    href: LocalHref | OutHref

@dataclass
class LocalButton:
    text: str
    href: LocalHref

@dataclass
class OutButton:
    text: str
    href: OutHref
