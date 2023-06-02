from sqlalchemy.orm import Session
from database import dbconnection, schemas
from model.productmodel import Product

def get_product_by_gtin(session: Session, gtin: str):
    return session.query(schemas.ProductSchema).filter(schemas.ProductSchema.gtin == gtin).first()


def get_product_all(session: Session):
    return session.query(schemas.ProductSchema).all()


def save_product(session: Session, product: Product):
    p = schemas.ProductSchema(**product.dict())
    session.add(p)
    session.commit()
    session.refresh(p)
    return p
