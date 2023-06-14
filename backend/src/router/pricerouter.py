from fastapi import APIRouter
from model.pricemodel import Price
from bussines.priceBussines import PriceBusiness


routerprice = APIRouter(prefix="/api/v1/prices")


@routerprice.post("")
async def set_price(price: Price):
    return await PriceBusiness.factory().save(price)
