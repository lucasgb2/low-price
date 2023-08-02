from pydantic import BaseModel, validator, Field, field_validator
from typing import Optional
from gtin.validator import is_valid_GTIN
from uuid import UUID, uuid4
from model.pricemodel import Price

class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    description: str = Optional[str]
    gtin: str = Optional[str]
    ncm: str = Optional[str]
    ncmDescription: str = Optional[str]
    linkimage: str = Optional[str]
    contrib: int = 0
    pricemax: Optional[Price] = None
    pricemin: Optional[Price] = None

    def to_id(self):
        return self.id.urn[9:]

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        exclude = {"pricemax", "pricemin"}

    @field_validator('gtin')
    def gtin_validator(cls, v):
        if not is_valid_GTIN(v):
            raise ValueError(f'The GTIN code ({v}) not is valid.')
        return v
