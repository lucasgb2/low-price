from model.pricemodel import Price
from dao.pricedao import PriceDAO
import humanize
from datetime import datetime


class PriceBusiness:


    async def save(self, price: Price):
        saved = await PriceDAO.factory().save_price(price)
        return saved

    async def get_prices_by_id_product(self, id_product: str):
        return await PriceDAO.factory().get_all_price_by_id_product(id_product)

    @classmethod
    def factory(self):
        return PriceBusiness()
