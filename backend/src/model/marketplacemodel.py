from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4


class Marketplace(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    place_id: Optional[int] = None
    name: Optional[str] = None
    city: Optional[str] = None
    longitude: float = Field(...)
    latitude: float = Field(...)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
