from model.contact import Contact

from dataclasses import dataclass

@dataclass
class ContactData:
    contacts: list[Contact]
