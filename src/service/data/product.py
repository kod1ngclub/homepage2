from model.product import Product

from dataclasses import dataclass

@dataclass
class ProductData:
    products: list[Product]
