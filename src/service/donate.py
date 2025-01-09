from model.donate import Donate

from view.donate import DonatePage
from view.donate import DonateCard

class DonateData:
    donates: list[Donate]

class DonateService:
    data: DonateData

    def __init__(self, data) -> None:
        self.data = data

    def Build(self) -> DonatePage:
        page = DonatePage()

        page.main.head      = self.data.donates[0].name
        page.main.href.to   = self.data.donates[0].href

        for item in self.data.donates[:1]:
            c           = DonateCard()
            c.head      = item.name
            c.href.to   = item.href

            page.subs.append(c)

        return page
