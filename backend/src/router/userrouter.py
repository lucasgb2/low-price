from fastapi import APIRouter, Depends, Response
from model.usermodel import User
from bussines.userbusiness import UserBusiness


routeruser = APIRouter(prefix="/api/v1/users")

@routeruser.post("")
async def set(user: User):
    r = await UserBusiness.factory().save(user)
    return r


@routeruser.get("/{email}", response_model=User)
async def get(email: str):
    return await UserBusiness.factory().get_byemail(email)


