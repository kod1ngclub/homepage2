from view.shared.href import OutHref

from enum import Enum

class DonateCard:
    head: str
    href: OutHref

class DonatePage:
    main: DonateCard
    subs: list[DonateCard]
