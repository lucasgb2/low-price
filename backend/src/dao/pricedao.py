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

    async def get_all_price_by_id_product(self, id_product: str):
        prices = await self.collection().find(filter=self.q('id_product', id_product)).to_list(10)
        pricesModel = []
        for p in prices:
            pricesModel.append(Price(**p))
        return pricesModel

    async def get_price_by_idproduct(self, idproduct: str):
        return await self.collection().find_one(filter=self.q('id_product', idproduct))


    async def get_max_price_by_product(self, idproduct: str) -> Price:
        p = await self.collection().find_one(filter={'id_product':idproduct}, sort=[("price", -1)], limit=1)
        if p is not None:
            return Price(**p)
        else:
            return None


    async def get_min_price_by_product(self, idproduct: str):
        p = await self.collection().find_one(filter={'id_product': idproduct}, sort=[("price", 1)], limit=1)
        if p is not None:
            return Price(**p)
        else:
            return None

    async def get_count_price(self, idproduct: str) -> int:
        r = await self.collection().count_documents(filter={'id_product': idproduct})
        return r
