from view.shared.href import OutHref
from view.shared.href import LocalHref

from view.landing import LandingPage
from view.product import ProductPage
from view.contact import ContactPage
from view.donate import DonatePage

from dataclasses import dataclass

# ==== components
@dataclass
class LocalItem:
    text: str
    href: LocalHref

@dataclass
class OutItem:
    text: str
    href: OutHref

# ==== layout
@dataclass
class Nav:
    items: list[LocalItem]

@dataclass
class Foot:
    table: list[LocalItem]
    family: list[OutItem]

# ==== page
@dataclass
class LandingGroup:
    index: LandingPage
    group: list[LandingPage] | None

@dataclass
class ProductGroup:
    index: ProductPage
    group: list[ProductPage] | None

@dataclass
class ContactGroup:
    index: ContactPage
    group: list[ContactPage] | None

@dataclass
class DonateGroup:
    index: DonatePage
    group: list[DonatePage] | None

# datapage
@dataclass
class DataPage:
    landing: LandingGroup
    product: ProductGroup
    contact: ContactGroup
    donate: DonateGroup

    nav: Nav
    foot: Foot
