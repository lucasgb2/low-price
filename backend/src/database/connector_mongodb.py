from threading import Lock
from motor.motor_asyncio import AsyncIOMotorClient
import os

class DBConnectionMetaClassSingleton(type):

    _instances = {}
    _lock: Lock = Lock()

    def __call__(self, *args, **kwargs):
        self._lock.acquire()
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        self._lock.release()
        return self._instances[self]

class DBConnection(metaclass=DBConnectionMetaClassSingleton):

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

