from pydantic import BaseModel, validator, Field
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
    pricemax: Optional[Price]
    pricemin: Optional[Price]

    def to_id(self):
        return self.id.urn[9:]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

    @validator('gtin')
    def gtin_validator(cls, v):
        if not is_valid_GTIN(v):
            raise ValueError(f'The GTIN code ({v}) not is valid.')
        return v
