from model.marketplacemodel import Marketplace
from dao.basedao import BaseDAO

class MarketplaceDAO(BaseDAO):

    def __init__(self):
        self.collection_name = 'marketplaces'

    async def get_marketplace_by_placeid(self, place_id: int):
        place =  await self.collection().find_one(self.q('place_id', place_id))
        return place

    async def save_marketplace(self, marketplace: Marketplace):
        saved = await self.collection().insert_one(marketplace)
        saved = await self.collection().find_one(self.qid(saved.inserted_id))
        return saved

    async def get_marketplace_all(self):
        return await self.collection().find().to_list(1000)

    @classmethod
    def factory(self):
        return MarketplaceDAO()