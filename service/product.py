from model.product import Product
from model.product import LevelName
from model.series import SeriesName

from service.data.product import ProductData

from view.product import ProductPage
from view.product import ProductCard
from view.product import Filter
from view.product import StarFiltered
from view.product import SeriesFiltered
from view.product import LevelFiltered


class ProductService:
    __data__: ProductData

    def __init__(self, data: ProductData) -> None:
        self.__data__ = data

    def Build(self) -> ProductPage:
        page = ProductPage(
            filter  = Filter(
                level   = LevelFiltered.NonFiltered,
                series  = SeriesFiltered.NonFiltered,
                star    = StarFiltered.NonFiltered
            ),
            cards   = []
        )

        for item in self.__data__.products:
            page.cards.append(
                ProductCard(
                    head    = item.name,
                    body    = item.description,
                    star    = item.star
                )
            )

        return page

    def BuildEach(self) -> list[ProductPage]:
        starconds       = list(StarFiltered)
        seriesconds     = list(SeriesFiltered)
        levelconds      = list(LevelFiltered)

        filterconds: list[Filter] = []
        for starcond in starconds:
            for seriescond in seriesconds:
                for levelcond in levelconds:
                    filterconds.append(Filter(
                        star        = starcond,
                        series      = seriescond,
                        level       = levelcond
                    ))

        pages: list[ProductPage] = []
        for filtercond in filterconds:
            page = ProductPage(filter=filtercond, cards=[])

            filtered: list[Product] = self.__data__.products
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
                page.cards.append(
                    ProductCard(
                        head    = item.name,
                        body    = item.description,
                        star    = item.star
                    )
                )

            pages.append(page)

        return pages
