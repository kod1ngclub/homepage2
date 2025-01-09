from model.contact import Contact
from model.contact import Media

from view.contact import ContactPage
from view.contact import ContactCard
from view.contact import Icon
from view.shared.href import OutHref

class ContactData:
    contacts: list[Contact]

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
            c = ContactCard(head="", href=OutHref(""), icon=Icon.Email)

            c.head = item.name
            c.href.to = item.href

            match item.media:
                case Media.Email:
                    c.icon = Icon.Email
                case Media.PhoneCall:
                    c.icon = Icon.PhoneCall
                case Media.LinkedIn:
                    c.icon = Icon.LinkedIn
                case Media.Discord:
                    c.icon = Icon.Discord
                case Media.Facebook:
                    c.icon = Icon.Facebook
                case Media.Twiiter:
                    c.icon = Icon.Twiiter
                case Media.Youtube:
                    c.icon = Icon.Youtube
                case Media.Blog:
                    c.icon = Icon.Blog
                case Media.Github:
                    c.icon = Icon.Github

            page.contacts.append(c)

        return page
