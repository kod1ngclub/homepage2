from model.product import Product
from model.series import SeriesName
from model.product import LevelName

from view.product import ProductPage
from view.product import ProductCard
from view.product import Filter
from view.product import StarFiltered
from view.product import SeriesFiltered
from view.product import LevelFiltered

class ProductData:
    products: list[Product]

class ProductService:
    data: ProductData

    def __init__(self, data: ProductData) -> None:
        self.data = data

    def BuildIndex(self) -> ProductPage:
        page = ProductPage()

        page.filter.star        = StarFiltered.NonFiltered
        page.filter.series      = SeriesFiltered.NonFiltered
        page.filter.level       = LevelFiltered.NotFiltered

        for item in self.data.products:
            c = ProductCard()
            c.head      = item.name
            c.body      = item.description
            c.star      = item.star

            page.cards.append(c)

        return page

    def BuildEach(self) -> list[ProductPage]:
        starconds       = list(StarFiltered)
        seriesconds     = list(SeriesFiltered)
        levelconds      = list(LevelFiltered)

        filterconds: list[Filter] = []
        for starcond in starconds:
            for seriescond in seriesconds:
                for levelcond in levelconds:
                    filtercond          = Filter()
                    filtercond.star     = starcond
                    filtercond.series   = seriescond
                    filtercond.level    = levelcond

        pages: list[ProductPage] = []
        for filtercond in filterconds:
            page = ProductPage()

            page.filter = filtercond

            filtered: list[Product] = self.data.products
            match filtercond.star:
                case StarFiltered.Star:
                    filtered = [item for item in filtered if (item.star == True)]
                case StarFiltered.NonStar:
                    filtered = [item for item in filtered if (item.star == False)]

            match filtercond.series:
                case SeriesFiltered.Host:
                    filtered = [item for item in filtered if (item.series == SeriesName.Host)]
                case SeriesFiltered.Cod:
                    filtered = [item for item in filtered if (item.series == SeriesName.Cod)]
                case SeriesFiltered.Etc:
                    filtered = [item for item in filtered if (item.series == SeriesName.Etc)]

            match filtercond.level:
                case LevelFiltered.Major:
                    filtered = [item for item in filtered if (item.level == LevelName.Major)]
                case LevelFiltered.Toy:
                    filtered = [item for item in filtered if (item.level == LevelName.Toy)]
                case LevelFiltered.Deprecated:
                    filtered = [item for item in filtered if (item.level == LevelName.Deprecated)]

            for item in filtered:
                c           = ProductCard()
                c.head      = item.name
                c.body      = item.description
                c.star      = item.star

                page.cards.append(c)

            pages.append(page)

        return pages
