from sqlalchemy.orm import Session
from database import dbconnection, schemas
from model.usermodel import User


def save_user(session: Session, user: User):
    u = schemas.UserSchema(**user.dict())
    session.add(u)
    session.commit()
    session.refresh(u)
    return

def get_user_byemail(session: Session, email:str):
    return session.query(schemas.UserSchema).filter(schemas.UserSchema.email == email).first()
