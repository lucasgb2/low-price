from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import dbconnection
from model.usermodel import User
from bussines.userbusiness import UserBusiness


def getBussines() -> UserBusiness:
    user_business: UserBusiness = UserBusiness()
    return user_business

routeruser = APIRouter(prefix="/api/v1/user")

@routeruser.post("")
def set(user: User, session: Session = Depends(dbconnection.get_dbsession)):
    return getBussines().save(session, user)


@routeruser.get("/{email}", response_model=User)
def get(email: str, session: Session = Depends(dbconnection.get_dbsession)):
    print(email)
    return getBussines().get_byemail(session, email)


