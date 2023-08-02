from fastapi import APIRouter
from model.pricemodel import Price
from bussines.priceBussines import PriceBusiness


routerprice = APIRouter(prefix="/api/v1/prices")


@routerprice.post("")
async def set_price(price: Price):
    return await PriceBusiness.factory().save(price)

@routerprice.get("/product/{id_product}")
async def get_prices_by_id_product(id_product: str):
    return await PriceBusiness.factory().get_prices_by_id_product(id_product)
