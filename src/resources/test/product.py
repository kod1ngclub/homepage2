from model.product import Product
from model.product import LevelName
from model.product import SeriesName

TEST_PRODUCTS: list[Product] = [
    Product(
        name            = "synote",
        description     = "Github oriented sharing note used in offline",
        href            = "https://www.example.com",

        level           = LevelName.Major,
        series          = SeriesName.Etc,
        star            = True
    ),
    Product(
        name            = "hostln",
        description     = "Selfhost blog app",
        href            = "https://www.example.com",

        level           = LevelName.Major,
        series          = SeriesName.Host,
        star            = True
    )
]
