from model.contact import Media

from service.data.contact import ContactData

from view.contact import ContactPage
from view.contact import ContactCard
from view.contact import Icon
from view.shared.href import OutHref

class ContactService:
    data: ContactData

    def __init__(self, data: ContactData) -> None:
        self.data = data

    def Build(self) -> ContactPage:
        page = ContactPage(
            contacts=[]
        )

        # push contact-cards
        for item in self.data.contacts:
            matchedicon: Icon = Icon.Email
            match item.media:
                case Media.Email:
                    matchedicon = Icon.Email
                case Media.PhoneCall:
                    matchedicon = Icon.PhoneCall
                case Media.LinkedIn:
                    matchedicon = Icon.LinkedIn
                case Media.Discord:
                    matchedicon = Icon.Discord
                case Media.Facebook:
                    matchedicon = Icon.Facebook
                case Media.Twiiter:
                    matchedicon = Icon.Twiiter
                case Media.Youtube:
                    matchedicon = Icon.Youtube
                case Media.Blog:
                    matchedicon = Icon.Blog
                case Media.Github:
                    matchedicon = Icon.Github


            page.contacts.append(
                ContactCard(
                    head    = item.name,
                    href    = OutHref(to=item.href),
                    icon    = matchedicon
                )
            )

        return page
