from service.data.landing import AboutImage, LandingData

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
        page.head = self.data.head
        page.body = self.data.body

        # section: about
        for item in self.data.abouts:
            page.abouts.append(
                AboutSection(
                    head    = item.head,
                    body    = item.body,
                    image   = Image(
                        source  = item.image.source,
                        alt     = item.image.alt
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
