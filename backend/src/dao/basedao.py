from database.connector_mongodb import get_connector
from pymongo import MongoClient
from pymongo.collection import Collection
from fastapi.encoders import jsonable_encoder

class BaseDAO:

    def __init__(self):
        self.collection_name = ''

    def conn(self) -> MongoClient:
        return get_connector()

    def collection(self) -> Collection:
        return self.conn()[self.collection_name]

    async def save(self, document):
        saved = await self.collection().insert_one(jsonable_encoder(document))
        saved = await self.collection().find_one(self.q('_id', saved.inserted_id))
        return saved

    def q(self, field: str, value: str) -> dict:
        return {field: value}

    def qid(self, id:str) -> dict:
        return {'_id' : id}

    def tojson(self, value):
        return jsonable_encoder(value)