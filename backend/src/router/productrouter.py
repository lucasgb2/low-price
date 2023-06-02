from typing import List, Union, Optional
from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.orm import Session
from database import dbconnection
from dao import productdao
from model.productmodel import Product
from bussines.productbusiness import ProductBusiness, getProductBusiness


routerproduct = APIRouter(prefix="/api/v1/products")


@routerproduct.post("")
async def set_product(product: Product, session: Session = Depends(dbconnection.get_dbsession)):
    return await getProductBusiness(session).save(product)

@routerproduct.get("/{gtin}", response_model=Product)
async def get_product(gtin: str, session: Session = Depends(dbconnection.get_dbsession)):
    return getProductBusiness(session).get_product_by_gtin(gtin)

@routerproduct.get("")
async def get_product(session: Session = Depends(dbconnection.get_dbsession)):
    return getProductBusiness(session).get_product_all()

@routerproduct.get("/{gtin}/prices")
async def get_product(gtin: str, session: Session = Depends(dbconnection.get_dbsession)):
    return getProductBusiness(session).get_price_by_product(gtin)

@routerproduct.get("/{gtin}/maxmin")
async def get_product(gtin: str, session: Session = Depends(dbconnection.get_dbsession)):
    return getProductBusiness(session).get_maxmin_price_by_gtin(gtin)