from view.shared.button import Button
from view.shared.button import OutButton
from view.shared.image import Image

from dataclasses import dataclass

@dataclass
class AboutSection:
    head: str
    body: str
    image: Image

@dataclass
class SeriesSection:
    head: str
    body: list[str]

@dataclass
class ProductSection:
    head: str
    body: list[str]
    button: OutButton
    image: Image

@dataclass
class FootSection:
    head: str
    buttons: list[Button]

@dataclass
class LandingPage:
    head: str
    body: str

    abouts: list[AboutSection]
    serieses: list[SeriesSection]
    products: list[ProductSection]
    foot: FootSection
