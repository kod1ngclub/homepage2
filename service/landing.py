from service.data.landing import AboutImage, LandingData

from view.landing import LandingPage
from view.landing import ProductSection
from view.landing import SeriesSection
from view.landing import AboutSection
from view.landing import FootSection
from view.shared.button import Button
from view.shared.button import OutButton
from view.shared.image import Image
from view.shared.href import OutHref
from view.shared.href import LocalHref

class LandingService:
    __data__: LandingData

    def __init__(self, data: LandingData) -> None:
        self.__data__ = data

    def Build(self) -> LandingPage:
        page = LandingPage(
            head        = self.__data__.head,
            body        = self.__data__.body,

            abouts      = [
                AboutSection(
                    head    = item.head,
                    body    = item.body,
                    image   = Image(
                        source  = item.image.source,
                        alt     = item.image.alt
                    )
                ) for item in self.__data__.abouts
            ],
            products    = [
                ProductSection(
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
                ) for item in self.__data__.products
            ],
            serieses    = [
                SeriesSection(
                    head    = item.name,
                    body    = item.description
                ) for item in self.__data__.serieses
            ],

            foot        = FootSection(
                head        = "Build something wonderful with us!",
                buttons     = [
                    Button(
                        text    = "Our Github",
                        href    = OutHref(to=self.__data__.github)
                    ),
                    Button(
                        text    = "Join us in Discord",
                        href    = OutHref(to=self.__data__.discord)
                    ),
                    Button(
                        text    = "More products",
                        href    = LocalHref.Product
                    )
                ]
            )
        )

        return page
