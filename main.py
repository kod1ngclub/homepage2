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
    path            = "/"
)