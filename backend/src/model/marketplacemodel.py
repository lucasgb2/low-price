from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4


class Marketplace(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    place_id: Optional[str]
    name: Optional[str]
    city: Optional[str]
    longitude: str = Field(...)
    latitude: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
