from pydantic import BaseModel, validator, Field, field_validator
from typing import Optional
from gtin.validator import is_valid_GTIN
from model.idfield import IdField

class Gtin(BaseModel):
    gtin: str = Field(...)

    @field_validator('gtin')
    def gtin_validator(cls, v):
        if not is_valid_GTIN(v):
            raise ValueError(f'The GTIN code ({v}) not is valid.')
        return v

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True


