from fastapi import APIRouter
from model.gtinmodel import Gtin
from bussines.productbusiness import ProductBusiness

routerproduct = APIRouter(prefix="/api/v1/products")

@routerproduct.post("")
async def set_product(gtin: Gtin):
    return await ProductBusiness.factory().save(gtin)

@routerproduct.get("/{gtin}")
async def get_product(gtin: str):
    return await ProductBusiness.factory().get_product_by_gtin(gtin)

@routerproduct.get("")
async def get_product():
    return await ProductBusiness.factory().get_product_all()

@routerproduct.get("/{gtin}/prices")
async def get_product(gtin: str):
    return await ProductBusiness.factory().get_price_by_gtin(gtin)