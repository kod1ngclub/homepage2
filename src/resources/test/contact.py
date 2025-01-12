from model.contact import Contact
from model.contact import Media

TEST_CONTACTS: list[Contact] = [
    Contact(
        name        = "Gmail",
        media       = Media.Email,
        href        = "mailto:someone@example.com"
    ),
    Contact(
        name        = "Discord",
        media       = Media.Discord,
        href        = "https://www.discord.example"
    )
]
