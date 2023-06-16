from pymongo import MongoClient
import motor.motor_asyncio
import os


'''
PASS_MONGO = '7qFwiieRMByzqQO2'
USER_MONGO = 'lowpricedb'
DB_MONGO = 'lowpricedb'
HOST_MONGO = 'clusterlowprice.fg2zoa8.mongodb.net'
'''

def get_envvar(envvar):
    if os.environ.get(envvar) is not None:
        return os.environ[envvar]
    else:
        return ''

def get_connector():
    password = get_envvar('PASSMONGO')
    user = get_envvar('USERMONGO')
    db = get_envvar('DBMONGO')
    host = get_envvar('HOSTMONGO')

    if True:
        connector = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority")
        c = connector[db]
        return c
    else:
        connector = MongoClient(f"mongodb+srv://{db}:{password}@{host}/?retryWrites=true&w=majority")
        return connector["lowprice"]





