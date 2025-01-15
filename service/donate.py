from resources.test import data
from service.data.donate import DonateData

from view.donate import DonatePage
from view.donate import DonateCard
from view.shared.href import OutHref

class DonateService:
    __data__: DonateData

    def __init__(self, data) -> None:
        self.__data__ = data

    def Build(self) -> DonatePage:
        page = DonatePage(main=DonateCard(head="", href=OutHref("")), subs=[])

        HEAD = self.__data__.donates[0]
        TAIL = self.__data__.donates[:1]

        page.main = DonateCard(
            head    = HEAD.name,
            href    = OutHref(to=HEAD.href)
        )

        for item in TAIL:
            page.subs.append(
                DonateCard(
                    head    = item.name,
                    href    = OutHref(to=item.href)
                )
            )

        return page
