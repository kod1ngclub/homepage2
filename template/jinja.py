from view.landing import LandingPage
from view.product import ProductPage
from view.product import LevelFiltered
from view.product import SeriesFiltered
from view.product import StarFiltered
from view.contact import ContactPage
from view.donate import DonatePage
from template.interface.datapage import Nav
from template.interface.datapage import Foot

from template.interface.engine import TemplateEngine
from template.interface.engine import TemplateConfig

from template.interface.datapage import DataPage

# lib
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template
from copy import deepcopy

from dataclasses import dataclass
from dataclasses import asdict
from enum import Enum

# ==== Constructor configs
@dataclass
class JinjaConfig:
    root: str
    landing: str
    product: str
    contact: str
    donate: str

@dataclass
class SitemapRoot:
    href: str

@dataclass
class SitemapSub:
    sub: str | None

@dataclass
class SitemapIndexConfig:
    root: str
    landing: str
    product: str
    contact: str
    donate: str

@dataclass
class RemotePNG:
    href: str
    width: int
    height: int
    alt: str

@dataclass
class RemotePNGIcon:
    href: str
    size: int

@dataclass
class HeadConfig:
    langcode: str

    icon16: RemotePNGIcon
    icon32: RemotePNGIcon
    icon64: RemotePNGIcon
    icon128: RemotePNGIcon
    icon256: RemotePNGIcon
    opengraph: RemotePNG

    author: str
    email: str

# ==== Filter to Word map for URL
class HrefLevelFilter(Enum):
    NonFiltered     = "levelf0"
    Major           = "levelf1"
    Toy             = "levelf2"
    Deprecated      = "levelf3"

class HrefSeriesFilter(Enum):
    NonFiltered     = "seriesf0"
    Host            = "seriesf1"
    Cod             = "seriesf2"
    Etc             = "seriesf3"

class HrefStarFilter(Enum):
    NonFiltered     = "starf0"
    Star            = "starf1"
    NonStar         = "starf2"

# ==== Jinja JSON format
@dataclass
class NavJSON:
    data: Nav

@dataclass
class FootJSON:
    data: Foot

@dataclass
class LandingJSON:
    index: LandingPage

@dataclass
class ProductFilterJSON:
    level: HrefLevelFilter
    series: HrefSeriesFilter
    star: HrefStarFilter

@dataclass
class ProductJSON:
    index: ProductPage
    filter: ProductFilterJSON | None

@dataclass
class ContactJSON:
    index: ContactPage

@dataclass
class DonateJSON:
    index: DonatePage

@dataclass
class DataJSON:
    nav: NavJSON
    foot: FootJSON
    landing: LandingJSON
    product: ProductJSON
    contact: ContactJSON
    donate: DonateJSON

@dataclass
class SitemapJSON:
    root: str
    landing: str
    product: str
    contact: str
    donate: str

@dataclass
class RemotePNGJSON:
    href: str
    width: int
    height: int
    alt: str

@dataclass
class RemotePNGIconJSON:
    href: str
    size: int

@dataclass
class HeadJSON:
    langcode: str

    icon16: RemotePNGIconJSON
    icon32: RemotePNGIconJSON
    icon64: RemotePNGIconJSON
    icon128: RemotePNGIconJSON
    icon256: RemotePNGIconJSON
    opengraph: RemotePNGJSON

    author: str
    email: str

@dataclass
class JinjaJSON:
    data: DataJSON
    sitemap: SitemapJSON
    head: HeadJSON

class JinjaTemplateEngine(TemplateEngine):
    __config__: TemplateConfig      = TemplateConfig(path="", debug=True)
    __configed__: bool              = False

    __jinja__: JinjaConfig
    __sitemap__: SitemapIndexConfig
    __head__: HeadConfig
    __static__: str

    def __init__(self, jinja: JinjaConfig, sitemap: SitemapIndexConfig, head: HeadConfig) -> None:
        self.__jinja__          = jinja
        self.__sitemap__        = sitemap
        self.__head__           = head

    def Init(self, config: TemplateConfig) -> None:
        if self.__configed__: return

        self.__config__         = config
        self.__configed__       = True

    def Run(self, datapage: DataPage) -> None:
        env: Environment            = Environment(loader=FileSystemLoader(self.__jinja__.root))

        landingtemp: Template       = env.get_template(self.__jinja__.landing)
        producttemp: Template       = env.get_template(self.__jinja__.product)
        contacttemp: Template       = env.get_template(self.__jinja__.contact)
        donatetemp: Template        = env.get_template(self.__jinja__.donate)

        ORIGIN = JinjaJSON(
            data = DataJSON(
                nav         = NavJSON(data=datapage.nav),
                foot        = FootJSON(data=datapage.foot),
                landing     = LandingJSON(index=datapage.landing.index),
                product     = ProductJSON(index=datapage.product.index, filter=None),
                contact     = ContactJSON(index=datapage.contact.index),
                donate      = DonateJSON(index=datapage.donate.index)
            ),
            sitemap = SitemapJSON(
                root        = self.__sitemap__.root,
                landing     = self.__sitemap__.landing,
                product     = self.__sitemap__.product,
                contact     = self.__sitemap__.contact,
                donate      = self.__sitemap__.donate
            ),
            head = HeadJSON(
                langcode    = self.__head__.langcode,

                author      = self.__head__.author,
                email       = self.__head__.email,

                icon16      = RemotePNGIconJSON(href=self.__head__.icon16.href, size=self.__head__.icon16.size),
                icon32      = RemotePNGIconJSON(href=self.__head__.icon32.href, size=self.__head__.icon32.size),
                icon64      = RemotePNGIconJSON(href=self.__head__.icon64.href, size=self.__head__.icon64.size),
                icon128     = RemotePNGIconJSON(href=self.__head__.icon128.href, size=self.__head__.icon128.size),
                icon256     = RemotePNGIconJSON(href=self.__head__.icon256.href, size=self.__head__.icon256.size),

                opengraph   = RemotePNGJSON(
                    href        = self.__head__.opengraph.href,
                    width       = self.__head__.opengraph.width,
                    height      = self.__head__.opengraph.height,
                    alt         = self.__head__.opengraph.alt
                )
            )
        )

        jsondata = deepcopy(ORIGIN)

        landinghtml: str    = landingtemp.render(asdict(jsondata))
        producthtml: str    = producttemp.render(asdict(jsondata))
        contacthtml: str    = contacttemp.render(asdict(jsondata))
        donatehtml: str     = donatetemp.render(asdict(jsondata))

        if datapage.product.group == None: raise Exception("'ProductPage' should have 'group'")

        producthtmls: list[str] = []
        for item in datapage.product.group:
            # match HrefLevelFilter
            hreflevel: HrefLevelFilter = HrefLevelFilter.NonFiltered

            match item.filter.level:
                case LevelFiltered.NonFiltered:
                    hreflevel = HrefLevelFilter.NonFiltered
                case LevelFiltered.Major:
                    hreflevel = HrefLevelFilter.Major
                case LevelFiltered.Toy:
                    hreflevel = HrefLevelFilter.Toy
                case LevelFiltered.Deprecated:
                    hreflevel = HrefLevelFilter.Deprecated
                case _:
                    raise Exception(f"level-filter data of datapage at JinjaTemplateEngine.Run() can't be {item.filter.level}")

            # match HrefSeriesFilter
            hrefseries: HrefSeriesFilter = HrefSeriesFilter.NonFiltered

            match item.filter.series:
                case SeriesFiltered.NonFiltered:
                    hrefseries = HrefSeriesFilter.NonFiltered
                case SeriesFiltered.Host:
                    hrefseries = HrefSeriesFilter.Host
                case SeriesFiltered.Cod:
                    hrefseries = HrefSeriesFilter.Cod
                case SeriesFiltered.Etc:
                    hrefseries = HrefSeriesFilter.Etc
                case _:
                    raise Exception(f"series-filter data of datapage at JinjaTemplateEngine.Run() can't be {item.filter.series}")

            # match HrefStarFilter
            hrefstar: HrefStarFilter = HrefStarFilter.NonFiltered

            match item.filter.star:
                case StarFiltered.NonFiltered:
                    hrefstar = HrefStarFilter.NonFiltered
                case StarFiltered.NonStar:
                    hrefstar = HrefStarFilter.NonStar
                case StarFiltered.Star:
                    hrefstar = HrefStarFilter.Star
                case _:
                    raise Exception(f"star-filter data of datapage at JinjaTemplateEngine.Run() can't be {item.filter.star}")

            jsondata = deepcopy(ORIGIN)

            jsondata.data.product.index = item
            jsondata.data.product.filter = ProductFilterJSON(
                level       = hreflevel,
                series      = hrefseries,
                star        = hrefstar
            )

            producthtmls.append(
                producttemp.render(asdict(jsondata))
            )

        print(landinghtml)
        print(producthtml)
        print(contacthtml)
        print(donatehtml)
        print("==================================")
        for item in producthtmls: print(item)

        print("Should make debug print for JinjaTemplateEngine")

        print("We run JinjaTemplateEngine")
