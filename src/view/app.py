from view.shared.href import OutHref
from view.shared.href import LocalHref


from view.landing import LandingPage
from view.product import ProductPage
from view.contact import ContactPage
from view.donate import DonatePage

# layout
class LocalItem:
    text: str
    href: LocalHref

class OutItem:
    text: str
    href: OutHref

class Nav:
    items: list[LocalItem]

class Foot:
    table: list[LocalItem]
    family: list[OutItem]

# group
class ProductGroup:
    index: ProductPage
    list[ProductPage]

# app
class App:
    landing: LandingPage
    product: ProductGroup
    contact: ContactPage
    donate: DonatePage

    nav: Nav
    foot: Foot
