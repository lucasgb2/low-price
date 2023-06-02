from pydantic import BaseModel, validator
import hashlib

class User(BaseModel):

    id: int = None
    name: str = ''
    email: str = ''
    password: str = ''

    class Config:
        orm_mode = True

    @validator('password')
    def convert_MD5_Password(cls, v: str):
        return hashlib.md5(v.encode('utf-8')).hexdigest()
