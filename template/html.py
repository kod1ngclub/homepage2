from template.interface.engine import TemplateEngine
from template.interface.engine import TemplateConfig

from template.interface.datapage import DataPage, Foot

# lib
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template

from dataclasses import asdict

class HTMLTemplateEngine(TemplateEngine):
    config: TemplateConfig      = TemplateConfig("")
    configed: bool              = False

    templateroot: str           = ""
    landingfile: str            = ""
    productfile: str            = ""
    contactfile: str            = ""
    donatefile: str             = ""

    def __init__(self, templateroot: str, landingfile: str, productfile: str, contactfile: str, donatefile: str) -> None:
        self.templateroot   = templateroot
        self.landingfile    = landingfile
        self.productfile    = productfile
        self.contactfile    = contactfile
        self.donatefile     = donatefile

    def Init(self, config: TemplateConfig) -> None:
        if self.configed: return

        self.config         = config
        self.configed       = True

    def Run(self, datapage: DataPage) -> None:
        env: Environment            = Environment(loader=FileSystemLoader(self.templateroot))

        landingtemp: Template       = env.get_template(self.landingfile)
        producttemp: Template       = env.get_template(self.productfile)
        contacttemp: Template       = env.get_template(self.contactfile)
        donatetemp: Template        = env.get_template(self.donatefile)

        normjson = {
            'nav':          asdict(datapage.nav),
            'foot':         asdict(datapage.foot),
            'landing':      asdict(datapage.landing),
            'product':      asdict(datapage.product.index),
            'contact':      asdict(datapage.contact),
            'donate':       asdict(datapage.donate)
        }

        landinghtml: str = landingtemp.render(normjson)
        producthtml: str = landingtemp.render(normjson)
        contacthtml: str = landingtemp.render(normjson)
        donatehtml: str = landingtemp.render(normjson)

        if datapage.product.group == None: raise Exception("'ProductPage' should have 'group'")

        producthtmls: list[str] = []
        for item in datapage.product.group:
            json = {
                'nav':      asdict(datapage.nav),
                'foot':     asdict(datapage.foot),
                'landing':  asdict(datapage.landing),
                'product':  asdict(item),
                'contact':  asdict(datapage.contact),
                'donate':   asdict(datapage.donate)
            }

            producthtmls.append(
                producttemp.render(json)
            )

        print("We run HTMLTemplateEngine")
