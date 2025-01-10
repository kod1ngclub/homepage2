from template.interface.engine import TemplateEngine
from template.interface.datapage import DataPage

def DELI(valname: str) -> str:
    return valname + ":"

def FIELD2(p: str, c1: str) -> str:
    return p + "." + c1

def FIELD3(p: str, c1: str, c2: str) -> str:
    return p + "." + c1 + "." + c2

def INDEX(arrname: str, index: int) -> str:
    return arrname + "[" + str(index) + "]"

def NEWLINE() -> None:
    print()

def SECTION(name: str) -> None:
    print("====", name)

class TestTemplateEngine(TemplateEngine):
    def Run(self, datapage: DataPage) -> None:
        nav         = datapage.nav
        foot        = datapage.foot

        landing     = datapage.landing
        product     = datapage.product
        contact     = datapage.contact
        donate      = datapage.donate

        SECTION("nav")

        for index, item in enumerate(nav.items):
            print(DELI(INDEX(FIELD2("nav", "items"), index)), item)

        NEWLINE()
        SECTION("foot")

        for index, item in enumerate(foot.table):
            print(DELI(INDEX(FIELD2("foot", "table"), index)), item)

        for index, item in enumerate(foot.family):
            print(DELI(INDEX(FIELD2("foot", "family"), index)), item)

        NEWLINE()
        SECTION("landing")

        print(DELI(FIELD2("landing", "head")), landing.index.head)
        print(DELI(FIELD2("landing", "body")), landing.index.body)

        for index, item in enumerate(landing.index.abouts):
            print(DELI(FIELD2(INDEX(FIELD2("landing", "abouts"), index), "head")), item.head)
            print(DELI(FIELD2(INDEX(FIELD2("landing", "abouts"), index), "body")), item.body)
            print(DELI(FIELD2(INDEX(FIELD2("landing", "abouts"), index), "image")), item.image)

        for index, item in enumerate(landing.index.products):
            print(DELI(FIELD2(INDEX(FIELD2("landing", "products"), index), "head")), item.head)
            print(DELI(FIELD2(INDEX(FIELD2("landing", "products"), index), "body")), item.body)
            print(DELI(FIELD2(INDEX(FIELD2("landing", "products"), index), "button")), item.button)
            print(DELI(FIELD2(INDEX(FIELD2("landing", "products"), index), "image")), item.image)

        for index, item in enumerate(landing.index.serieses):
            print(DELI(FIELD2(INDEX(FIELD2("landing", "serieses"), index), "head")), item.head)
            print(DELI(FIELD2(INDEX(FIELD2("landing", "serieses"), index), "body")), item.body)

        NEWLINE()
        SECTION("product")

        print(DELI(FIELD3("product", "filter", "star")), product.index.filter.star)
        print(DELI(FIELD3("product", "filter", "series")), product.index.filter.series)
        print(DELI(FIELD3("product", "filter", "level")), product.index.filter.level)

        for index, item in enumerate(product.index.cards):
            print(DELI(FIELD2(INDEX(FIELD2("product", "cards"), index), "head")), item.head)
            print(DELI(FIELD2(INDEX(FIELD2("product", "cards"), index), "body")), item.body)
            print(DELI(FIELD2(INDEX(FIELD2("product", "cards"), index), "star")), item.star)

        NEWLINE()
        SECTION("product - group")

        if product.group == None:
            print("'ProductPage' should have 'group'")
            return

        for prodindex, proditem in enumerate(product.group):
            PROD = INDEX(FIELD2("product", "group"), prodindex)

            print(DELI(FIELD3(PROD, "filter", "star")), proditem.filter.star)
            print(DELI(FIELD3(PROD, "filter", "series")), proditem.filter.series)
            print(DELI(FIELD3(PROD, "filter", "level")), proditem.filter.level)

            for index, item in enumerate(proditem.cards):
                print(DELI(FIELD2(INDEX(FIELD2(PROD, "cards"), index), "head")), item.head)
                print(DELI(FIELD2(INDEX(FIELD2(PROD, "cards"), index), "body")), item.body)
                print(DELI(FIELD2(INDEX(FIELD2(PROD, "cards"), index), "star")), item.star)


        NEWLINE()
        SECTION("contact")

        for index, item in enumerate(contact.index.contacts):
            print(DELI(FIELD2(INDEX(FIELD2("contact", "contacts"), index), "head")), item.head)
            print(DELI(FIELD2(INDEX(FIELD2("contact", "contacts"), index), "href")), item.href)
            print(DELI(FIELD2(INDEX(FIELD2("contact", "contacts"), index), "icon")), item.icon)

        NEWLINE()
        SECTION("donate")

        print(DELI(FIELD3("donate", "main", "head")), donate.index.main.head)
        print(DELI(FIELD3("donate", "main", "href")), donate.index.main.href)

        for index, item in enumerate(donate.index.subs):
            print(DELI(FIELD2(INDEX(FIELD2("donate", "subs"), index), "head")), item.head)
            print(DELI(FIELD2(INDEX(FIELD2("donate", "subs"), index), "href")), item.href)
