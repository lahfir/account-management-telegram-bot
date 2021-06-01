import pymongo
from pymongo import MongoClient
from datetime import datetime

from pymongo.errors import DuplicateKeyError

cluster = MongoClient(
    "mongodb+srv://lahfir:mslahfir%40262001@clustertms.lkxcy.mongodb.net/test?authSource=admin&replicaSet=atlas-xqmx6k-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
)
if cluster:
    print("Connected")

db = cluster["tms"]
collection = db["test"]

try:
    results = collection.insert_one({"_id": 0, "name": "lahfir", "date": datetime.now()})

except DuplicateKeyError as dke:
    print(dke)