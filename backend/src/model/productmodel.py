from pydantic import BaseModel, validator
from gtin.validator import is_valid_GTIN

class Product(BaseModel):
    id: int = None
    description: str = ''
    gtin: str
    ncm: str = ''
    ncmDescription: str = ''
    linkimage: str = ''


    class Config:
        orm_mode = True

    @validator('gtin')
    def gtin_validator(cls, v):
        if not is_valid_GTIN(v):
            raise ValueError(f'The GTIN code ({v}) not is valid.')
        return v
