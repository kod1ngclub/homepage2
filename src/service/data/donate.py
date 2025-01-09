from model.donate import Donate

from dataclasses import dataclass

@dataclass
class DonateData:
    donates: list[Donate]
