from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
import os

class DBConnection:

    def __init__(self):
        self.connection = None

    def get_envvar(self, envvar):
        if os.environ.get(envvar) is not None:
            return os.environ[envvar]
        else:
            return ''

    def get_connector(self):
        password = self.get_envvar('PASSMONGO')
        user = self.get_envvar('USERMONGO')
        dbname = self.get_envvar('DBMONGO')
        host = self.get_envvar('HOSTMONGO')

        if self.connection == None:
            print('Nova conexão')
            self.connection = AsyncIOMotorClient(f"mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority")
        db = self.connection[dbname]
        return db

dbconnection = DBConnection()

