# service - data
from service.landing import LandingData
from service.product import ProductData
from service.contact import ContactData
from service.donate import DonateData

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

from view.app import App
from view.app import Nav
from view.app import Foot
from view.app import LocalItem
from view.app import OutItem

from view.shared.href import LocalHref
from view.shared.href import OutHref

# engine
from template.interface import TemplateEngine
from template.test import TestTemplateEngine

# ==== data-fetching
landingdata: LandingData        = LandingData()
productdata: ProductData        = ProductData()
contactdata: ContactData        = ContactData()
donatedata: DonateData          = DonateData()

# ==== build pages
landingserv: LandingService     = LandingService(landingdata)
productserv: ProductService     = ProductService(productdata)
contactserv: ContactService     = ContactService(contactdata)
donateserv: DonateService       = DonateService(donatedata)

landingpage: LandingPage        = landingserv.Build()
productindex: ProductPage       = productserv.BuildIndex()
productgroup: list[ProductPage] = productserv.BuildEach()
contactpage: ContactPage        = contactserv.Build()
donatepage: DonatePage          = donateserv.Build()

# ==== bind app
app: App        = App()

nav: Nav        = Nav()
nav.items.append(LocalItem())
nav.items.append(LocalItem())
nav.items.append(LocalItem())
nav.items.append(LocalItem())

nav.items[0].text       = "Home"
nav.items[0].href       = LocalHref.Landing

nav.items[1].text       = "Product"
nav.items[1].href       = LocalHref.Product

nav.items[2].text       = "Contact"
nav.items[2].href       = LocalHref.Contact

nav.items[3].text       = "Donate"
nav.items[3].href       = LocalHref.Donate

foot: Foot      = Foot()

foot.table.append(LocalItem())
foot.table.append(LocalItem())
foot.table.append(LocalItem())
foot.table.append(LocalItem())

foot.table[0].text      = "Home"
foot.table[0].href      = LocalHref.Landing

foot.table[1].text      = "Product"
foot.table[1].href      = LocalHref.Product

foot.table[2].text      = "Contact"
foot.table[2].href      = LocalHref.Contact

foot.table[3].text      = "Donate"
foot.table[3].href      = LocalHref.Donate

foot.family.append(OutItem())
foot.family.append(OutItem())

foot.family[0].text     = "Google"
foot.family[0].href.to  = "https://www.google.com"

foot.family[1].text     = "Example"
foot.family[1].href.to  = "https://www.example.com"

app.landing             = landingpage
app.product.index       = productindex
app.product.group       = productgroup
app.contact             = contactpage
app.donate              = donatepage

app.nav                 = nav
app.foot                = foot

# ==== render pages (with engine)
engine: TemplateEngine  = TestTemplateEngine()
engine.Run(app)
