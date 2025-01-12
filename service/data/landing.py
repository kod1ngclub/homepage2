from dataclasses import dataclass

@dataclass
class AboutImage:
    source: str
    alt: str

@dataclass
class About:
    head: str
    body: str
    image: AboutImage

@dataclass
class ProductImage:
    source: str
    alt: str

@dataclass
class ProductExample:
    name: str
    description: list[str]
    href: str
    image: ProductImage

@dataclass
class SeriesExample:
    name: str
    description: list[str]

@dataclass
class LandingData:
    head: str
    body: str
    abouts: list[About]
    products: list[ProductExample]
    serieses: list[SeriesExample]
    github: str
    discord: str
