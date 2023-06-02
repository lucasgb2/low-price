from model.marketplacemodel import Marketplace
from dao import marketplacedao
from service.geoplaceservice import GeoPlaceService
from sqlalchemy.orm import Session


class MarketplaceBusiness:

    def __init__(self, marketplace: Marketplace):
        self.marketplace: Marketplace = marketplace

    async def save_marketplace(self, session: Session):
        if self.marketplace.id == None:
            await self.fill_marketplace_information()
        marketplace_saved = marketplacedao.get_marketplace_by_placeid(session, self.marketplace.place_id)
        if marketplace_saved:
            return marketplace_saved
        else:
            return marketplacedao.save_marketplace(session, self.marketplace)

    async def fill_marketplace_information(self):
        geo: GeoPlaceService = GeoPlaceService(self.marketplace.longitude, self.marketplace.latitude)
        await geo.fill()
        self.marketplace = geo.marketplace
        return True
