from sqlalchemy.orm import Session
from sqlalchemy import func, text
from database import dbconnection, schemas
from model.pricemodel import Price
from fastapi import encoders

def save_price(session: Session, price: Price):
    print(price.dict())
    u = schemas.PriceSchema(**price.dict())
    session.add(u)
    session.commit()
    session.refresh(u)
    return u

def get_price_by_product(session: Session, idproduct: int):
    r = session.query(schemas.PriceSchema)\
        .filter(schemas.PriceSchema.id_product == idproduct)\
        .order_by(schemas.PriceSchema.price.asc()).all()
    return r
def get_max_min_price_by_product(session: Session, idproduct: int):
    sql = f" select 'max' as type, max(pp.price) as price, pp.* from productprice pp where id_product = {idproduct} "+\
          " union "+\
          f" select 'min' as type, min(pp.price) as price, pp.* from productprice pp where id_product = {idproduct} "

    dataset = session.execute(text(sql))
    result = []
    for d in dataset:
        result.append(encoders.jsonable_encoder(d))
    return result
