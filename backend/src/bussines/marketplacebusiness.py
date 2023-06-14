from model.marketplacemodel import Marketplace
from dao.marketplacedao import MarketplaceDAO
from service.geoplaceservice import GeoPlaceService
from fastapi.encoders import jsonable_encoder


class MarketplaceBusiness:

    async def save_marketplace(self, marketplace: Marketplace):
        if marketplace.place_id == None:
            marketplace = await self.fill_marketplace_information(marketplace)
        saved = await MarketplaceDAO.factory().get_marketplace_by_placeid(marketplace.place_id)
        if saved:
            return saved
        else:
            return await MarketplaceDAO.factory().save_marketplace(jsonable_encoder(marketplace))

    async def get_marketplace(self):
        return await MarketplaceDAO.factory().get_marketplace_all()

    async def fill_marketplace_information(self, marketplace: Marketplace):
        geo: GeoPlaceService = GeoPlaceService(marketplace.longitude, marketplace.latitude)
        await geo.fill()
        return geo.marketplace

    @classmethod
    def factory(self):
        return MarketplaceBusiness()
