import pymongo
from pymongo import MongoClient
from datetime import datetime

from pymongo.errors import DuplicateKeyError

cluster = MongoClient(
    "mongodb+srv://lahfir:mslahfir%40262001@clustertms.lkxcy.mongodb.net/test?authSource=admin&replicaSet=atlas-xqmx6k-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
)
if cluster:
    print("Connected")

db = cluster["Signals"]
collection = db["06-30-2021"]

try:
    data = collection.find()
    for i in data:
        print(i["ticker"])
except DuplicateKeyError as dke:
    print(dke)

