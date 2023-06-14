from model.usermodel import User
from dao.basedao import BaseDAO
from fastapi.encoders import jsonable_encoder


class UserDAO(BaseDAO):

    def __init__(self):
        self.collection_name = 'users'

    @classmethod
    def factory(self):
        return UserDAO()

    async def save_user(self, user: User) -> User:
        saved = await self.collection().insert_one(jsonable_encoder(user))
        saved = await self.collection().find_one(self.q('_id', saved.inserted_id))
        return saved

    async def get_user_byemail(self, email: str) -> User:
        saved = await self.collection().find_one(self.q('email', email))
        return saved
