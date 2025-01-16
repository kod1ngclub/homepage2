# data
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
from view.shared.image import Image

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

from template.interface.engine import TemplateEngine
from template.interface.engine import TemplateConfig
from template.test import TestTemplateEngine
from template.jinja import JinjaTemplateEngine

from template.jinja import JinjaConfig
from template.jinja import SitemapIndexConfig
from template.jinja import SitemapRoot
from template.jinja import SitemapSub
from template.jinja import HeadConfig
from template.jinja import RemotePNG
from template.jinja import RemotePNGIcon

# resources
from resources.test.data import TEST_HEAD
from resources.test.data import TEST_BODY
from resources.test.data import TEST_ABOUTS
from resources.test.data import TEST_EXAMPLE_PRODUCTS
from resources.test.data import TEST_EXAMPLE_SERIESES
from resources.test.data import TEST_GITHUB
from resources.test.data import TEST_DISCORD
from resources.test.product import TEST_PRODUCTS
from resources.test.contact import TEST_CONTACTS
from resources.test.donate import TEST_DONATES

# lib
from pathlib import Path

def Build(landingdata: LandingData, productdata: ProductData, contactdata: ContactData, donatedata: DonateData, engine: TemplateEngine, conf: TemplateConfig):
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
    engine.Init(conf)
    engine.Run(datapage=page)

# def filepath words
WORD_BUILD: str             = "build"
WORD_RESOURCES: str         = "resources"
WORD_TEMPLATE: str          = "template"
WORD_STATIC: str            = "static"
WORD_LAYOUT: str            = "layout.html"
WORD_LANDING: str           = "landing.html"
WORD_PRODUCT: str           = "product.html"
WORD_CONTACT: str           = "contact.html"
WORD_DONATE: str            = "donate.html"

# def filepath constants
FILEPATH_BUILD: Path                             = Path.cwd().joinpath(WORD_BUILD)
FILEPATH_RESOURCES_TEMPLATE: Path                = Path.cwd().joinpath(WORD_RESOURCES).joinpath(WORD_TEMPLATE)
FILEPATH_RESOURCES_STATIC: Path                  = Path.cwd().joinpath(WORD_RESOURCES).joinpath(WORD_STATIC)
FILEPATH_RESOURCES_TEMPLATE_LAYOUT: Path         = FILEPATH_RESOURCES_TEMPLATE.joinpath(WORD_LAYOUT)
FILEPATH_RESOURCES_TEMPLATE_LANDING: Path        = FILEPATH_RESOURCES_TEMPLATE.joinpath(WORD_LANDING)
FILEPATH_RESOURCES_TEMPLATE_PRODUCT: Path        = FILEPATH_RESOURCES_TEMPLATE.joinpath(WORD_PRODUCT)
FILEPATH_RESOURCES_TEMPLATE_CONTACT: Path        = FILEPATH_RESOURCES_TEMPLATE.joinpath(WORD_CONTACT)
FILEPATH_RESOURCES_TEMPLATE_DONATE: Path         = FILEPATH_RESOURCES_TEMPLATE.joinpath(WORD_DONATE)

# check usable
def FAIL_TO_FIND(path: Path):   return (not path.exists())
def TO_STR(path: Path):         return str(path)

if FAIL_TO_FIND(FILEPATH_BUILD):                        raise Exception(f"Filepath {TO_STR(FILEPATH_BUILD)} not exist")
if FAIL_TO_FIND(FILEPATH_RESOURCES_STATIC):             raise Exception(f"Filepath {TO_STR(FILEPATH_RESOURCES_STATIC)} not exist")
if FAIL_TO_FIND(FILEPATH_RESOURCES_TEMPLATE):           raise Exception(f"Filepath {TO_STR(FILEPATH_RESOURCES_TEMPLATE)} not exist")
if FAIL_TO_FIND(FILEPATH_RESOURCES_TEMPLATE_LAYOUT):    raise Exception(f"Filepath {TO_STR(FILEPATH_RESOURCES_TEMPLATE_LAYOUT)} not exist")
if FAIL_TO_FIND(FILEPATH_RESOURCES_TEMPLATE_LANDING):   raise Exception(f"Filepath {TO_STR(FILEPATH_RESOURCES_TEMPLATE_LANDING)} not exist")
if FAIL_TO_FIND(FILEPATH_RESOURCES_TEMPLATE_PRODUCT):   raise Exception(f"Filepath {TO_STR(FILEPATH_RESOURCES_TEMPLATE_PRODUCT)} not exist")
if FAIL_TO_FIND(FILEPATH_RESOURCES_TEMPLATE_CONTACT):   raise Exception(f"Filepath {TO_STR(FILEPATH_RESOURCES_TEMPLATE_CONTACT)} not exist")
if FAIL_TO_FIND(FILEPATH_RESOURCES_TEMPLATE_DONATE):    raise Exception(f"Filepath {TO_STR(FILEPATH_RESOURCES_TEMPLATE_DONATE)} not exist")

Build(
    landingdata     = LandingData(
        head            = TEST_HEAD,
        body            = TEST_BODY,
        abouts          = TEST_ABOUTS,
        products        = TEST_EXAMPLE_PRODUCTS,
        serieses        = TEST_EXAMPLE_SERIESES,
        github          = TEST_GITHUB,
        discord         = TEST_DISCORD
    ),
    productdata     = ProductData(products=TEST_PRODUCTS),
    contactdata     = ContactData(contacts=TEST_CONTACTS),
    donatedata      = DonateData(donates=TEST_DONATES),
    engine          = JinjaTemplateEngine(
        jinja = JinjaConfig(
            root        = TO_STR(FILEPATH_RESOURCES_TEMPLATE),
            landing     = WORD_LANDING,
            product     = WORD_PRODUCT,
            contact     = WORD_CONTACT,
            donate      = WORD_DONATE
        ),
        sitemap = SitemapIndexConfig(
            root        = "https://www.example.com",
            landing     = "https://www.example.com",
            product     = "https://www.example.com/product",
            contact     = "https://www.example.com/contact",
            donate      = "https://www.example.com/donate"
        ),
        head = HeadConfig(
            langcode    = "ko",

            icon16      = RemotePNGIcon(href="https://www.example.com/icon16.png", size=16),
            icon32      = RemotePNGIcon(href="https://www.example.com/icon16.png", size=32),
            icon64      = RemotePNGIcon(href="https://www.example.com/icon16.png", size=64),
            icon128     = RemotePNGIcon(href="https://www.example.com/icon16.png", size=128),
            icon256     = RemotePNGIcon(href="https://www.example.com/icon16.png", size=256),

            author      = "authorname",
            email       = "someone@example.com",

            opengraph   = RemotePNG(
                href        = "https://www.example.com/opengraph.png",
                width       = 1200,
                height      = 600,
                alt         = "Opengraph image of website"
            )
        )
    ),
    conf = TemplateConfig(
        path    = TO_STR(FILEPATH_BUILD),
        debug   = True
    )
)
