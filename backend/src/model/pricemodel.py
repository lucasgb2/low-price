from pydantic import BaseModel, validator
from datetime import datetime

class Price(BaseModel):

    id: int = None
    id_product: int = None
    id_marketplace: int = None
    price: float = 0
    moment: datetime


    class Config:
        orm_mode = True
