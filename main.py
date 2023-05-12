#!/usr/bin/python3

from pymongo import MongoClient

connectionString = "mongodb://localhost:27017/"
client = MongoClient(connectionString)
db = client["db_restaurant"]
collection = db["restaurants"]
print("Alle Stadtbezirke:")
for borough in collection.distinct("borough"):
    print("- " + borough)
