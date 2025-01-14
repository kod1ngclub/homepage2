from template.interface.engine import TemplateEngine
from template.interface.engine import TemplateConfig

from template.interface.datapage import DataPage, Foot

# lib
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template

from dataclasses import asdict

class HTMLTemplateEngine(TemplateEngine):
    __config__: TemplateConfig      = TemplateConfig("")
    __configed__: bool              = False

    __templateroot__: str           = ""
    __landingfile__: str            = ""
    __productfile__: str            = ""
    __contactfile__: str            = ""
    __donatefile__: str             = ""

    def __init__(self, templateroot: str, landingfile: str, productfile: str, contactfile: str, donatefile: str) -> None:
        self.__templateroot__   = templateroot
        self.__landingfile__    = landingfile
        self.__productfile__    = productfile
        self.__contactfile__    = contactfile
        self.__donatefile__     = donatefile

    def Init(self, config: TemplateConfig) -> None:
        if self.__configed__: return

        self.__config__         = config
        self.__configed__       = True

    def Run(self, datapage: DataPage) -> None:
        env: Environment            = Environment(loader=FileSystemLoader(self.__templateroot__))

        landingtemp: Template       = env.get_template(self.__landingfile__)
        producttemp: Template       = env.get_template(self.__productfile__)
        contacttemp: Template       = env.get_template(self.__contactfile__)
        donatetemp: Template        = env.get_template(self.__donatefile__)

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
