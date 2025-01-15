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

from template.jinja import JinjaTemplateEngine
from template.jinja import JinjaConfig
from template.jinja import SitemapIndexConfig

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

def Build(landingdata: LandingData, productdata: ProductData, contactdata: ContactData, donatedata: DonateData, engine: TemplateEngine):
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
    engine.Run(datapage=page)

# template filepath words
WORD_RESOURCES: str         = "resources"
WORD_TEMPLATE: str          = "template"
WORD_LAYOUT: str            = "layout.html"
WORD_LANDING: str           = "landing.html"
WORD_PRODUCT: str           = "product.html"
WORD_CONTACT: str           = "contact.html"
WORD_DONATE: str            = "donate.html"

# define filepaths as 'Path'
RESOURCES_TEMPLATE: Path                = Path.cwd().joinpath(WORD_RESOURCES).joinpath(WORD_TEMPLATE)
RESOURCES_TEMPLATE_LAYOUT: Path         = RESOURCES_TEMPLATE.joinpath(WORD_LAYOUT)
RESOURCES_TEMPLATE_LANDING: Path        = RESOURCES_TEMPLATE.joinpath(WORD_LANDING)
RESOURCES_TEMPLATE_PRODUCT: Path        = RESOURCES_TEMPLATE.joinpath(WORD_PRODUCT)
RESOURCES_TEMPLATE_CONTACT: Path        = RESOURCES_TEMPLATE.joinpath(WORD_CONTACT)
RESOURCES_TEMPLATE_DONATE: Path         = RESOURCES_TEMPLATE.joinpath(WORD_DONATE)

# check usable
def FAIL_TO_FIND(path: Path): return (not path.exists())
def TO_FILEPATH(path: Path): return str(path)

if FAIL_TO_FIND(RESOURCES_TEMPLATE):            raise Exception(f"Fielpath {TO_FILEPATH(RESOURCES_TEMPLATE)} not exist")
if FAIL_TO_FIND(RESOURCES_TEMPLATE_LAYOUT):     raise Exception(f"Fielpath {TO_FILEPATH(RESOURCES_TEMPLATE_LAYOUT)} not exist")
if FAIL_TO_FIND(RESOURCES_TEMPLATE_LANDING):    raise Exception(f"Fielpath {TO_FILEPATH(RESOURCES_TEMPLATE_LANDING)} not exist")
if FAIL_TO_FIND(RESOURCES_TEMPLATE_PRODUCT):    raise Exception(f"Fielpath {TO_FILEPATH(RESOURCES_TEMPLATE_PRODUCT)} not exist")
if FAIL_TO_FIND(RESOURCES_TEMPLATE_CONTACT):    raise Exception(f"Fielpath {TO_FILEPATH(RESOURCES_TEMPLATE_CONTACT)} not exist")
if FAIL_TO_FIND(RESOURCES_TEMPLATE_DONATE):     raise Exception(f"Fielpath {TO_FILEPATH(RESOURCES_TEMPLATE_DONATE)} not exist")

engine: TemplateEngine = JinjaTemplateEngine(
    jinja = JinjaConfig(
        root        = TO_FILEPATH(RESOURCES_TEMPLATE),
        landing     = WORD_LANDING,
        product     = WORD_PRODUCT,
        contact     = WORD_CONTACT,
        donate      = WORD_DONATE
    ),
    sitemap = SitemapIndexConfig(
        root        = "https://www.example.com",
        landing     = None,
        product     = "product",
        contact     = "contact",
        donate      = "donate"
    )
)
engine.Init(TemplateConfig(path="/build", debug=True))

Build(
    landingdata     = LandingData(
        head        = TEST_HEAD,
        body        = TEST_BODY,
        abouts      = TEST_ABOUTS,
        products    = TEST_EXAMPLE_PRODUCTS,
        serieses    = TEST_EXAMPLE_SERIESES,
        github      = TEST_GITHUB,
        discord     = TEST_DISCORD
    ),
    productdata     = ProductData(products=TEST_PRODUCTS),
    contactdata     = ContactData(contacts=TEST_CONTACTS),
    donatedata      = DonateData(donates=TEST_DONATES),
    engine          = engine
)
