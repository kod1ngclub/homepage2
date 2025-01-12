from service.data.donate import DonateData

from view.donate import DonatePage
from view.donate import DonateCard
from view.shared.href import OutHref

class DonateService:
    data: DonateData

    def __init__(self, data) -> None:
        self.data = data

    def Build(self) -> DonatePage:
        page = DonatePage(main=DonateCard(head="", href=OutHref("")), subs=[])

        page.main = DonateCard(
            head    = self.data.donates[0].name,
            href    = OutHref(to=self.data.donates[0].href)
        )

        for item in self.data.donates[:1]:
            page.subs.append(
                DonateCard(
                    head    = item.name,
                    href    = OutHref(to=item.href)
                )
            )

        return page
