from service.data.landing import LandingData

from view.landing import LandingPage
from view.landing import ProductSection
from view.landing import SeriesSection
from view.landing import AboutSection
from view.landing import FootSection
from view.shared.button import Button, OutButton
from view.shared.image import Image
from view.shared.href import OutHref
from view.shared.href import LocalHref

class LandingService:
    data: LandingData

    def __init__(self, data: LandingData) -> None:
        self.data = data

    def Build(self) -> LandingPage:
        page = LandingPage(
            head        = "",
            body        = "",
            abouts      = [],
            products    = [],
            serieses    = [],
            foot        = FootSection(
                head        = "",
                buttons     = []
            )
        )

        # section: jumbotron
        page.head = "Kod1ngclub"
        page.body = "코딩 동아리를 위한 코딩 동아리"

        # section: about
        page.abouts.append(
            AboutSection(
                head    = "Why we do this?",
                body    = "새 학기가 시작되고 야심찬 마음으로 코딩 동아리에 가입합니다. 첫 날부터 기술 스택 선정에 8시간을 태웠습니다. 개발자들은 C와 Python으로 나누어서 파벌 전쟁을 벌이고 있습니다. 뭐 그게 중요하겠습니까? 아무튼 프로젝트는 시작됬습니다. 기획자는 오늘도 새로운 기획안을 가져옵니다. 젠장, 기획서는 거의 뭐 카카오가 따로 없습니다. 1px만 옮겨달라는 디자이너의 울부짖음도 무시할 수는 없겠죠? 그렇게 6개월이 흐릅니다. 이런! 학기 말이 다가오지만 아무것도 이루어 진게 없습니다. 이게 몇 번째 인지 모르겠습니다.누군가가 이걸 막아줄 수는 없을까요?",
                image   = Image(
                    source  = "https://www.example.com",
                    alt     = "An image with angry developers, designer requesting 1px-move and project manager only making more things-to-do"
                )
            )
        )

        page.abouts.append(
            AboutSection(
                head    = "How to solve it?",
                body    = "이미 많은 경험이 있는 개발자들이 기술 스택을 대신 정해준다면 어떨까요? 기획과 협업을 위한 교육과 프로젝트 툴은 어떨까요? 디자이너들이 더 개발자 입장에서 사고할 수 있다면 이 문제가 해결되지 않을까요? 그래서 Kod1ngclub은 저희의 서비스를 해결책으로 제시합니다.우리의 툴과 코드는 완전히 무료이며, 라이센스를 준수한다면 일절 개입하지 않습니다.고민 없이 적용하고 성취해 내세요. 두 번째 Kod1ngclub의 등장이 Kod1ngclub의 목표입니다.",
                image   = Image(
                    source  = "https://www.example.com",
                    alt     = "A question mark image"
                )
            )
        )

        # section: products
        for item in self.data.products:
            page.products.append(ProductSection(
                head    = item.name,
                body    = item.description,
                button  = OutButton(
                    href    = OutHref(to=item.href),
                    text    = "More"
                ),
                image   = Image(
                    source  = item.image.source,
                    alt     = item.image.alt
                )
            ))

        # section: serieses
        for item in self.data.serieses:
            page.serieses.append(SeriesSection(
                head    = item.name,
                body    = item.description
            ))

        # section: foot
        page.foot.head = "Build something wonderful with us!"

        page.foot.buttons.append(
            Button(
                text    = "Our Github",
                href    = OutHref(to=self.data.github)
            )
        )

        page.foot.buttons.append(
            Button(
                text    = "Join us in Discord",
                href    = OutHref(to=self.data.discord)
            )
        )

        page.foot.buttons.append(
            Button(
                text    = "More products",
                href    = LocalHref.Product
            )
        )

        return page
