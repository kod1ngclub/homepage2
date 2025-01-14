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
class SitemapIndexConfig:
    root: str
    landing: str | None
    product: str | None
    contact: str | None
    donate: str | None

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
    landing: str | None
    product: str | None
    contact: str | None
    donate: str | None

@dataclass
class JinjaJSON:
    data: DataJSON
    sitemap: SitemapJSON

class JinjaTemplateEngine(TemplateEngine):
    __config__: TemplateConfig      = TemplateConfig("")
    __configed__: bool              = False

    __jinja__: JinjaConfig
    __sitemap__: SitemapIndexConfig

    def __init__(self, jinja: JinjaConfig, sitemap: SitemapIndexConfig) -> None:
        self.__jinja__          = jinja
        self.__sitemap__        = sitemap

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

        jsondata = JinjaJSON(
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
                donate      = self.__sitemap__.donate,
            )
        )

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

            jsondata = JinjaJSON(
                data = DataJSON(
                    nav         = NavJSON(data=datapage.nav),
                    foot        = FootJSON(data=datapage.foot),
                    landing     = LandingJSON(index=datapage.landing.index),
                    product     = ProductJSON(
                        index       = item,
                        filter      = ProductFilterJSON(
                            level       = hreflevel,
                            series      = hrefseries,
                            star        = hrefstar
                        )
                    ),
                    contact     = ContactJSON(index=datapage.contact.index),
                    donate      = DonateJSON(index=datapage.donate.index)
                ),
                sitemap = SitemapJSON(
                    root        = self.__sitemap__.root,
                    landing     = self.__sitemap__.landing,
                    product     = self.__sitemap__.product,
                    contact     = self.__sitemap__.contact,
                    donate      = self.__sitemap__.donate,
                )
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

        print("We run JinjaTemplateEngine")
