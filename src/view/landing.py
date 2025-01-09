from view.shared.button import Button
from view.shared.button import OutButton
from view.shared.image import Image

class AboutSection:
    head: str
    body: str
    image: Image

class SeriesSection:
    head: str
    body: list[str]

class ProductSection:
    head: str
    body: list[str]
    button: OutButton
    image: Image

class FootSection:
    head: str
    buttons: list[Button]

class LandingPage:
    head: str
    body: str

    abouts: list[AboutSection]
    serieses: list[SeriesSection]
    products: list[ProductSection]
    foot: FootSection
