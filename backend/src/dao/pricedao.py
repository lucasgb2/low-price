from model.pricemodel import Price
from dao.basedao import BaseDAO

class PriceDAO(BaseDAO):
    def __init__(self):
        self.collection_name = 'prices'

    async def save_price(self, price: Price):
        return await self.save(price)
    @classmethod
    def factory(self):
        return PriceDAO()

    async def get_price_by_idproduct(self, idproduct: str):
        r = await self.collection().find_one(filter=self.q('id_product', idproduct))
        return r

    async def get_max_price_by_product(self, idproduct: str):
        r = await self.collection().find_one(filter={'id_product':idproduct}, sort=[("price", -1)], limit=1)
        return r

    async def get_min_price_by_product(self, idproduct: str):
        return await self.collection().find_one(filter={'id_product':idproduct}, sort=[("price", 1)], limit=1)