from model.pricemodel import Price
from dao.pricedao import PriceDAO
import humanize
from datetime import datetime


class PriceBusiness:

    def convert_moment_human(self, price: Price) -> Price:
        price.moment_human = humanize.naturaldelta(datetime.now() - price.moment)
        return price

    async def save(self, price: Price):
        price = self.convert_moment_human(price)
        saved = await PriceDAO.factory().save_price(price)
        return saved

    @classmethod
    def factory(self):
        return PriceBusiness()
