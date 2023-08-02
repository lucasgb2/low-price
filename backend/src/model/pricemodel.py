from pydantic import BaseModel, Field, root_validator, model_validator
from datetime import datetime
from model.marketplacemodel import Marketplace
from uuid import UUID, uuid4
from typing import Optional
import humanize


class Price(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    id_product: str = Field(...)
    marketplace: Optional[Marketplace]
    price: float = Field(default=0)
    moment: datetime
    moment_human: Optional[str] = ''

    @model_validator(mode='after')
    def convert_moment_human(cls, values):
        m = values.moment
        v = humanize.naturaltime(datetime.now() - m)
        values.moment_human = v
        return values



    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
