from sqlalchemy import Boolean, Column, Integer, String, BigInteger, Float, DateTime, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from .dbconnection import Base


class ProductSchema(Base):
    __tablename__ = "product"

    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True, index=True)
    description = Column(String)
    gtin = Column(String)
    ncm = Column(String)
    ncmDescription = Column(String)
    linkimage = Column(String)

class MarketplaceSchema(Base):
    __tablename__ = "marketplace"

    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True, index=True)
    place_id = Column(Integer)
    name = Column(String)
    city = Column(String)
    longitude = Column(String)
    latitude = Column(String)

class UserSchema(Base):
    __tablename__ = "user"

    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class PriceSchema(Base):
    __tablename__ = "productprice"

    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True, index=True)
    id_product = Column(Integer, ForeignKey('product.id'))
    id_marketplace = Column(Integer, ForeignKey('marketplace.id'))
    price = Column(Float)
    moment = Column(DateTime)

