import json
from pydantic import BaseModel, Field, PyObject

from datetime import datetime
from model.marketplacemodel import Marketplace
from uuid import UUID, uuid4
from typing import Optional


class Price(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    id_product: str = Field(...)
    marketplace: Optional[Marketplace]
    price: float = Field(default=0)
    moment: datetime
    moment_human: Optional[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
