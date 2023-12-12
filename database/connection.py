from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()


DB_NAME = os.getenv("DATABASE_NAME")

DB_PASSWORD = os.getenv("DATABASE_PASSWORD")

uri = f"mongodb+srv://{DB_NAME}:{DB_PASSWORD}@fastapi.rbrejkl.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(uri)


db = client.test_db

category = db["category"]

post = db["post"]

user = db["user"]
