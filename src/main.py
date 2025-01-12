# model
from model.product import Product
from model.product import LevelName
from model.product import SeriesName
from model.contact import Contact
from model.contact import Media
from model.donate import Donate

# service - data
from service.data.landing import LandingData
from service.data.landing import ProductExample
from service.data.landing import SeriesExample
from service.data.landing import ProductImage
from service.data.product import ProductData
from service.data.contact import ContactData
from service.data.donate import DonateData

# service
from service.landing import LandingService
from service.product import ProductService
from service.contact import ContactService
from service.donate import DonateService

# view-model
from view.landing import LandingPage
from view.product import ProductPage
from view.contact import ContactPage
from view.donate import DonatePage

from view.shared.href import LocalHref
from view.shared.href import OutHref

# engine
from template.interface.datapage import DataPage
from template.interface.datapage import LandingGroup
from template.interface.datapage import ProductGroup
from template.interface.datapage import ContactGroup
from template.interface.datapage import DonateGroup

from template.interface.datapage import Nav
from template.interface.datapage import Foot
from template.interface.datapage import LocalItem
from template.interface.datapage import OutItem

from template.interface.engine import TemplateConfig, TemplateEngine
from template.test import TestTemplateEngine
from view.shared.image import Image


def Build(landingdata: LandingData, productdata: ProductData, contactdata: ContactData, donatedata: DonateData, path: str):
    # Init service
    landingserv: LandingService         = LandingService(data=landingdata)
    productserv: ProductService         = ProductService(data=productdata)
    contactserv: ContactService         = ContactService(data=contactdata)
    donateserv: DonateService           = DonateService(data=donatedata)

    # Build pages
    landingpage: LandingPage            = landingserv.Build()
    productindex: ProductPage           = productserv.Build()
    productgroup: list[ProductPage]     = productserv.BuildEach()
    contactpage: ContactPage            = contactserv.Build()
    donatepage: DonatePage              = donateserv.Build()

    # Bind to datapage
    page: DataPage = DataPage(
        landing = LandingGroup(
            index       = landingpage,
            group       = None
        ),
        product = ProductGroup(
            index       = productindex,
            group       = productgroup
        ),
        contact = ContactGroup(
            index       = contactpage,
            group       = None
        ),
        donate = DonateGroup(
            index       = donatepage,
            group       = None
        ),

        nav = Nav(
            items = [
                LocalItem(text="Home", href=LocalHref.Root),
                LocalItem(text="Product", href=LocalHref.Product),
                LocalItem(text="Contact", href=LocalHref.Contact),
                LocalItem(text="Donate", href=LocalHref.Donate)
            ]
        ),
        foot = Foot(
            table = [
                LocalItem(text="Home", href=LocalHref.Root),
                LocalItem(text="Product", href=LocalHref.Product),
                LocalItem(text="Contact", href=LocalHref.Contact),
                LocalItem(text="Donate", href=LocalHref.Donate)
            ],
            family = [
                OutItem(text="Google", href=OutHref(to="https://www.google.com")),
                OutItem(text="Example", href=OutHref(to="https://www.example.com"))
            ]
        )
    )

    # Render with engine
    engine: TemplateEngine = TestTemplateEngine()
    engine.Init(TemplateConfig(
        path = path
    ))

    engine.Run(datapage=page)

l: LandingData = LandingData(
    products = [
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
    ],
    serieses = [
        SeriesExample(
            name            = "host",
            description     = ["Selfhost toolset", "Used in any platform"]
        )
    ],
    github = "https://www.example.com",
    discord = "https://www.example.com"
)

p: ProductData = ProductData(
    products = [
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
        ),
    ]
)

c: ContactData = ContactData(
    contacts = [
        Contact(
            name        = "Gmail",
            media       = Media.Email,
            href        = "mailto:someone@example.com"
        ),
        Contact(
            name        = "Discord",
            media       = Media.Discord,
            href        = "https://www.discord.example"
        )
    ]
)

d: DonateData = DonateData(
    donates = [
        Donate(
            name        = "Buy me a coffee",
            href        = "https://www.buymeacoffee.com"
        ),
        Donate(
            name        = "Kakao",
            href        = "https://www.example.com"
        )
    ]
)

Build(
    landingdata     = l,
    productdata     = p,
    contactdata     = c,
    donatedata      = d,
    path            = "/"
)
