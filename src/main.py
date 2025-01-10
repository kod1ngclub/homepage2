# service - data
from service.data.landing import LandingData
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

from template.interface.engine import TemplateEngine
from template.test import TestTemplateEngine

# ==== data-fetching
landingdata: LandingData        = LandingData(products=[], serieses=[], github="", discord="")
productdata: ProductData        = ProductData(products=[])
contactdata: ContactData        = ContactData(contacts=[])
donatedata: DonateData          = DonateData(donates=[])

# ==== build pages
landingserv: LandingService     = LandingService(data=landingdata)
productserv: ProductService     = ProductService(data=productdata)
contactserv: ContactService     = ContactService(data=contactdata)
donateserv: DonateService       = DonateService(data=donatedata)

landingpage: LandingPage        = landingserv.Build()
productindex: ProductPage       = productserv.Build()
productgroup: list[ProductPage] = productserv.BuildEach()
contactpage: ContactPage        = contactserv.Build()
donatepage: DonatePage          = donateserv.Build()

# ==== bind datapage
page: DataPage = DataPage(
    landing     = LandingGroup(
        index       = landingpage,
        group       = None
    ),
    product     = ProductGroup(
        index       = productindex,
        group       = productgroup
    ),
    contact     = ContactGroup(
        index       = contactpage,
        group       = None
    ),
    donate      = DonateGroup(
        index       = donatepage,
        group       = None
    ),

    nav         = Nav(
        items=[
            LocalItem(text="Home", href=LocalHref.Root),
            LocalItem(text="Product", href=LocalHref.Product),
            LocalItem(text="Contact", href=LocalHref.Contact),
            LocalItem(text="Donate", href=LocalHref.Donate)
        ]
    ),
    foot        = Foot(
        table=[
            LocalItem(text="Home", href=LocalHref.Root),
            LocalItem(text="Product", href=LocalHref.Product),
            LocalItem(text="Contact", href=LocalHref.Contact),
            LocalItem(text="Donate", href=LocalHref.Donate)
        ],
        family=[
            OutItem(text="Google", href=OutHref(to="https://www.google.com")),
            OutItem(text="Example", href=OutHref(to="https://www.example.com"))
        ]
    )
)

# ==== render pages (with engine)
engine: TemplateEngine  = TestTemplateEngine()
engine.Run(datapage=page)
