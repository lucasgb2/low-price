from typing import List, Union, Optional
from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.orm import Session
from database import dbconnection
from dao import pricedao
from model.pricemodel import Price
from bussines.priceBussines import getBusinessPrice


routerprice = APIRouter(prefix="/api/v1/prices")


@routerprice.post("")
async def set_product(price: Price, session: Session = Depends(dbconnection.get_dbsession)):
    return getBusinessPrice(session).save(price)
