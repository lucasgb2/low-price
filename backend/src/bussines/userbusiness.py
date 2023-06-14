from model.usermodel import User
from dao.userdao import UserDAO
from fastapi.responses import JSONResponse
from fastapi import status

class UserBusiness:
    @classmethod
    def factory(self):
        return UserBusiness()

    async def save(self, user: User):
        saved = await UserDAO.factory().save_user(user)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=saved)

    async def get_byemail(self, email:str):
        user = await UserDAO.factory().get_user_byemail(email)
        return JSONResponse(status_code=status.HTTP_200_OK, content=user)