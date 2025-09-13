
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "assessment_db")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]


employees_collection = db["employees"]
users_collection = db["users"]