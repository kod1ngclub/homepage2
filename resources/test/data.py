from service.data.landing import About
from service.data.landing import AboutImage
from service.data.landing import ProductExample
from service.data.landing import SeriesExample
from service.data.landing import ProductImage

TEST_HEAD       = "Name of team"
TEST_BODY       = "Description of team"

TEST_ABOUTS: list[About] = [
    About(
        head    = "About section Head 01",
        body    = "Blablabla",
        image   = AboutImage(source="https://www.example.com", alt="Example")
    ),
    About(
        head    = "About section Head 02",
        body    = "Blablabla",
        image   = AboutImage(source="https://www.example.com", alt="Example")
    )
]

TEST_EXAMPLE_PRODUCTS: list[ProductExample] = [
    ProductExample(
        name            = "Product 01",
        description     = ["Bla", "Blabla", "Blablabla"],
        href            = "https://www.example.com",
        image           = ProductImage(source="https://www.example.com", alt="Example")
    ),
    ProductExample(
        name            = "Product 02",
        description     = ["Bla", "Blabla", "Blablabla"],
        href            = "https://www.example.com",
        image           = ProductImage(source="https://www.example.com", alt="Example")
    )
]

TEST_EXAMPLE_SERIESES: list[SeriesExample] = [
    SeriesExample(
        name            = "Series 01",
        description     = ["Bla", "Blabla"]
    )
]

TEST_GITHUB = "https://www.example.com"
TEST_DISCORD = "https://www.example.com"
