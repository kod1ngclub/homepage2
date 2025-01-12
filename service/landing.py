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
