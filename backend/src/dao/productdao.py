from model.productmodel import Product
from dao.basedao import BaseDAO


class ProductDAO(BaseDAO):

    def __init__(self):
        self.collection_name = 'products'

    async def get_product_by_gtin(self, gtin: str) -> Product:
        r = await self.collection().find_one(self.q('gtin', gtin))
        if r is not None:
            return Product(**r)
        else:
            return None

    async def get_product_by_ncm(self, ncm: str) -> Product:
        return await self.collection().find(self.q('ncm', ncm)).to_list(10)

    async def get_product_all(self):
        return await self.collection().find().to_list(1000)

    async def save_product(self, product: Product):
        k = self.tojson(product)
        saved = await self.collection().insert_one(k)
        saved = await self.collection().find_one(self.qid(saved.inserted_id))
        return saved

    @classmethod
    def factory(self):
        return ProductDAO()