from motor.motor_asyncio import AsyncIOMotorClient
from data.config import DB_NAME, DB_USER, DB_PASS

srv = "mongodb+srv://{}:{}@cluster0.vrvwe.azure.mongodb.net/{}?retryWrites=true&w=majority"

db = AsyncIOMotorClient(srv.format(DB_PASS, DB_USER, DB_NAME))[DB_NAME]

users = db.users
groups = db.groups