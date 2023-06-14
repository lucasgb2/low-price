from fastapi import APIRouter, Depends, Response
from model.marketplacemodel import Marketplace
from bussines.marketplacebusiness import MarketplaceBusiness

routermarketplace = APIRouter(prefix="/api/v1/marketplaces")

@routermarketplace.post("")
async def set_marketplace(marketplace: Marketplace):
    if marketplace.longitude != '':
        return await MarketplaceBusiness.factory().save_marketplace(marketplace)

@routermarketplace.get("")
async def get_marketplace():
    return await MarketplaceBusiness.factory().get_marketplace()