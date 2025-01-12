from service.data.landing import About
from service.data.landing import AboutImage
from service.data.landing import ProductExample
from service.data.landing import SeriesExample
from service.data.landing import ProductImage

TEST_HEAD       = "Some Team"
TEST_BODY       = "Some Body"

TEST_ABOUTS: list[About] = [
    About(
        head    = "Why we do this?",
        body    = "Blablabla",
        image   = AboutImage(source="https://www.example.com", alt="Example")
    ),
    About(
        head    = "How to solve it?",
        body    = "Blablabla",
        image   = AboutImage(source="https://www.example.com", alt="Example")
    )
]

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
