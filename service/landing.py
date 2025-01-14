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
    __data__: LandingData

    def __init__(self, data: LandingData) -> None:
        self.__data__ = data

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
        page.head = self.__data__.head
        page.body = self.__data__.body

        # section: about
        for item in self.__data__.abouts:
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
        for item in self.__data__.products:
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
        for item in self.__data__.serieses:
            page.serieses.append(SeriesSection(
                head    = item.name,
                body    = item.description
            ))

        # section: foot
        page.foot.head = "Build something wonderful with us!"

        page.foot.buttons.append(
            Button(
                text    = "Our Github",
                href    = OutHref(to=self.__data__.github)
            )
        )

        page.foot.buttons.append(
            Button(
                text    = "Join us in Discord",
                href    = OutHref(to=self.__data__.discord)
            )
        )

        page.foot.buttons.append(
            Button(
                text    = "More products",
                href    = LocalHref.Product
            )
        )

        return page
