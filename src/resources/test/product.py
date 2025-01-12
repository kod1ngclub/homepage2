from model.product import Product
from model.product import LevelName
from model.product import SeriesName

TEST_PRODUCTS: list[Product] = [
    Product(
        name            = "Product 01",
        description     = "Blablabla",
        href            = "https://www.example.com",

        level           = LevelName.Major,
        series          = SeriesName.Etc,
        star            = True
    ),
    Product(
        name            = "Product 02",
        description     = "Blablabla",
        href            = "https://www.example.com",

        level           = LevelName.Toy,
        series          = SeriesName.Host,
        star            = True
    ),
    Product(
        name            = "Product 03",
        description     = "Blablabla",
        href            = "https://www.example.com",

        level           = LevelName.Toy,
        series          = SeriesName.Cod,
        star            = True
    ),
    Product(
        name            = "Product 04",
        description     = "Blablabla",
        href            = "https://www.example.com",

        level           = LevelName.Deprecated,
        series          = SeriesName.Host,
        star            = False
    ),
    Product(
        name            = "Product 04",
        description     = "Blablabla",
        href            = "https://www.example.com",

        level           = LevelName.Deprecated,
        series          = SeriesName.Etc,
        star            = False
    ),
    Product(
        name            = "Product 05",
        description     = "Blablabla",
        href            = "https://www.example.com",

        level           = LevelName.Toy,
        series          = SeriesName.Host,
        star            = True
    ),
    Product(
        name            = "Product 06",
        description     = "Blablabla",
        href            = "https://www.example.com",

        level           = LevelName.Toy,
        series          = SeriesName.Cod,
        star            = False
    ),
]
