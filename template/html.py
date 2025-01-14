from template.interface.engine import TemplateEngine
from template.interface.engine import TemplateConfig

from template.interface.datapage import DataPage

class HTMLTemplateEngine(TemplateEngine):
    config: TemplateConfig      = TemplateConfig("")
    configed: bool              = False

    landingpath: str            = ""
    productpath: str            = ""
    contactpath: str            = ""
    donatepath: str             = ""

    def __init__(self, landingpath: str, productpath: str, contactpath: str, donatepath: str) -> None:
        self.landingpath    = landingpath
        self.productpath    = productpath
        self.contactpath    = contactpath
        self.donatepath     = donatepath

    def Init(self, config: TemplateConfig) -> None:
        if self.configed: return

        self.config         = config
        self.configed       = True

    def Run(self, datapage: DataPage) -> None:
        print("We run HTMLTemplateEngine")
