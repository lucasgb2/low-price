from sqlalchemy.orm import Session
from database import dbconnection, schemas
from model.marketplacemodel import Marketplace

def get_marketplace_by_placeid(session: Session, place_id: int) -> Marketplace:
    return session.query(schemas.MarketplaceSchema).filter(schemas.MarketplaceSchema.place_id == place_id).first()

def save_marketplace(session: Session, marketplace: Marketplace):
    m = schemas.MarketplaceSchema(**marketplace.dict())
    session.add(m)
    session.commit()
    session.refresh(m)
    return m
