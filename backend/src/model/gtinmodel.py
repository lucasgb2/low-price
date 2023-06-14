from pydantic import BaseModel, validator, Field
from typing import Optional
from gtin.validator import is_valid_GTIN
from model.idfield import IdField

class Gtin(BaseModel):
    gtin: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {IdField: str}

    @validator('gtin')
    def gtin_validator(cls, v):
        if not is_valid_GTIN(v):
            raise ValueError(f'The GTIN code ({v}) not is valid.')
        return v
