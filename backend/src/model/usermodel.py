from pydantic import BaseModel, validator, Field
from model.idfield import IdField
import hashlib
from uuid import UUID, uuid4

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


    @validator('password')
    def convert_MD5_Password(cls, v: str):
        return hashlib.md5(v.encode('utf-8')).hexdigest()
