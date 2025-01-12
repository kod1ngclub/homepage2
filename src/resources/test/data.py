from service.data.landing import ProductExample
from service.data.landing import SeriesExample
from service.data.landing import ProductImage

TEST_EXAMPLE_PRODUCTS: list[ProductExample] = [
    ProductExample(
        name            = "synote",
        description     = ["Github-oriented sharing note", "Can use in offline"],
        href            = "https://www.example.com",
        image           = ProductImage(source="https://www.example.com", alt="Example")
    ),
    ProductExample(
        name            = "hostln",
        description     = ["Selfhost blog CMS", "Line-based document", "Portability"],
        href            = "https://www.example.com",
        image           = ProductImage(source="https://www.example.com", alt="Example")
    )
]

TEST_EXAMPLE_SERIESES: list[SeriesExample] = [
    SeriesExample(
        name            = "host",
        description     = ["Selfhost toolset", "Used in any platform"]
    )
]

TEST_GITHUB = "https://www.example.com"
TEST_DISCORD = "https://www.example.com"
