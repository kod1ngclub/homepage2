from view.landing import LandingPage
from view.landing import ProductSection
from view.landing import SeriesSection
from view.landing import AboutSection

from view.shared.button import Button
from view.shared.href import OutHref
from view.shared.href import LocalHref

class ProductImage:
    source: str
    alt: str

class ProductExample:
    name: str
    description: list[str]
    href: str
    image: ProductImage

class SeriesExample:
    name: str
    description: list[str]

class LandingData:
    products: list[ProductExample]
    serieses: list[SeriesExample]
    github: str
    discord: str

class LandingService:
    data: LandingData

    def __init__(self, data: LandingData) -> None:
        self.data = data

    def Build(self) -> LandingPage:
        page = LandingPage()

        # section: jumbotron
        page.head = "Kod1ngclub"
        page.body = "코딩 동아리를 위한 코딩 동아리"

        # section: about
        page.abouts.append(AboutSection())
        page.abouts.append(AboutSection())

        page.abouts[0].head             = "Why we do this?"
        page.abouts[0].body             = "새 학기가 시작되고 야심찬 마음으로 코딩 동아리에 가입합니다. 첫 날부터 기술 스택 선정에 8시간을 태웠습니다. 개발자들은 C와 Python으로 나누어서 파벌 전쟁을 벌이고 있습니다. 뭐 그게 중요하겠습니까? 아무튼 프로젝트는 시작됬습니다. 기획자는 오늘도 새로운 기획안을 가져옵니다. 젠장, 기획서는 거의 뭐 카카오가 따로 없습니다. 1px만 옮겨달라는 디자이너의 울부짖음도 무시할 수는 없겠죠? 그렇게 6개월이 흐릅니다. 이런! 학기 말이 다가오지만 아무것도 이루어 진게 없습니다. 이게 몇 번째 인지 모르겠습니다.누군가가 이걸 막아줄 수는 없을까요?"
        page.abouts[0].image.source     = "https://www.example.com"
        page.abouts[0].image.alt        = "An image with angry developers, designer requesting 1px-move and project manager only making more things-to-do"

        page.abouts[1].head             = "How to solve it?"
        page.abouts[1].body             = "이미 많은 경험이 있는 개발자들이 기술 스택을 대신 정해준다면 어떨까요? 기획과 협업을 위한 교육과 프로젝트 툴은 어떨까요? 디자이너들이 더 개발자 입장에서 사고할 수 있다면 이 문제가 해결되지 않을까요? 그래서 Kod1ngclub은 저희의 서비스를 해결책으로 제시합니다.우리의 툴과 코드는 완전히 무료이며, 라이센스를 준수한다면 일절 개입하지 않습니다.고민 없이 적용하고 성취해 내세요. 두 번째 Kod1ngclub의 등장이 Kod1ngclub의 목표입니다."
        page.abouts[1].image.source     = "https://www.example.com"
        page.abouts[1].image.alt        = "A question mark image"

        # section: products
        for item in self.data.products:
            s                   = ProductSection()
            s.head              = item.name
            s.body              = item.description
            s.image.source      = item.image.source
            s.image.alt         = item.image.alt
            s.button.href.to    = item.href
            s.button.text       = "More"

            page.products.append(s)

        # section: serieses
        for item in self.data.serieses:
            s               = SeriesSection()
            s.head          = item.name
            s.body          = item.description

            page.serieses.append(s)

        # section: foot
        page.foot.head = "Build something wonderful with us!"

        page.foot.buttons.append(Button())
        page.foot.buttons.append(Button())
        page.foot.buttons.append(Button())

        gh: OutHref                 = OutHref()
        gh.to                       = self.data.github
        page.foot.buttons[0].href   = gh
        page.foot.buttons[0].text   = "Our Github"

        dis: OutHref                = OutHref()
        dis.to                      = self.data.discord
        page.foot.buttons[1].href   = dis
        page.foot.buttons[1].text   = "Join us in Discord"

        prod: LocalHref             = LocalHref.Product
        page.foot.buttons[2].href   = prod
        page.foot.buttons[2].text   = "See more products"

        return page