from model.pricemodel import Price
from dao.pricedao import PriceDAO
from fastapi.responses import JSONResponse


class PriceBusiness:

    async def save(self, price: Price):
        saved = await PriceDAO.factory().save_price(price)
        return saved

    @classmethod
    def factory(self):
        return PriceBusiness()
