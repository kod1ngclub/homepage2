from view.shared.href import OutHref
from view.shared.href import LocalHref


from view.landing import LandingPage
from view.product import ProductPage
from view.contact import ContactPage
from view.donate import DonatePage

from dataclasses import dataclass

# layout
@dataclass
class LocalItem:
    text: str
    href: LocalHref

@dataclass
class OutItem:
    text: str
    href: OutHref

@dataclass
class Nav:
    items: list[LocalItem]

@dataclass
class Foot:
    table: list[LocalItem]
    family: list[OutItem]

# group
@dataclass
class ProductGroup:
    index: ProductPage
    group: list[ProductPage]

# app
@dataclass
class App:
    landing: LandingPage
    product: ProductGroup
    contact: ContactPage
    donate: DonatePage

    nav: Nav
    foot: Foot
