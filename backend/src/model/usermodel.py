from pydantic import BaseModel, validator, Field, field_validator
from model.idfield import IdField
import hashlib
from uuid import UUID, uuid4

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True


    @field_validator('password')
    def convert_MD5_Password(cls, v: str):
        return hashlib.md5(v.encode('utf-8')).hexdigest()
