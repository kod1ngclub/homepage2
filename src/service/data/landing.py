from dataclasses import dataclass

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
    products: list[ProductExample]
    serieses: list[SeriesExample]
    github: str
    discord: str
