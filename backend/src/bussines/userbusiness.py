from model.usermodel import User
from dao import userdao
from sqlalchemy.orm import Session


class UserBusiness:

    def save(self, session: Session, user: User) -> User:
        user_saved = userdao.save_user(session, user)
        if user_saved:
            return user_saved
        else:
            return None

    def get_byemail(self, session: Session, email:str):
        return userdao.get_user_byemail(session, email)