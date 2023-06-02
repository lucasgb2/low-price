from pydantic import BaseModel

class Marketplace(BaseModel):
    id: int = None
    place_id: int = 0
    name: str = ''
    city: str = ''
    longitude: str = ''
    latitude: str = ''

    class Config:
        orm_mode = True
