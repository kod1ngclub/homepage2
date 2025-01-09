from view.shared.href import LocalHref
from view.shared.href import OutHref

class Button:
    text: str
    href: LocalHref | OutHref

class LocalButton:
    text: str
    href: LocalHref

class OutButton:
    text: str
    href: OutHref
