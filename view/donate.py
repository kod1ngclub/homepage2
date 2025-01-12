from view.shared.href import OutHref

from dataclasses import dataclass
from enum import Enum

@dataclass
class DonateCard:
    head: str
    href: OutHref

@dataclass
class DonatePage:
    main: DonateCard
    subs: list[DonateCard]
