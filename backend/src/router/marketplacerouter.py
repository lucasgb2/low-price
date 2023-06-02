from typing import List
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import dbconnection
from model.marketplacemodel import Marketplace
from bussines.marketplacebusiness import MarketplaceBusiness

routermarketplace = APIRouter(prefix="/api/v1/marketplace")

@routermarketplace.post("")
async def set_marketplace(marketplace: Marketplace, session: Session = Depends(dbconnection.get_dbsession)):
    print('----------')
    print(marketplace)
    print('----------')
    if marketplace.longitude != '':
        marketplacebusiness: MarketplaceBusiness = MarketplaceBusiness(marketplace)
        return await marketplacebusiness.save_marketplace(session)
    else:
        return ''
