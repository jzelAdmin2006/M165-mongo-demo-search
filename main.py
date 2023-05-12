#!/usr/bin/python3

from pymongo import MongoClient

connectionString = "mongodb://localhost:27017/"
client = MongoClient(connectionString)
db = client["db_restaurant"]
collection = db["restaurants"]
print("Alle Stadtbezirke:")
for borough in collection.distinct("borough"):
    print("- " + borough)

print("Top 3 restaurants mit höchstem Rating:")
for restaurant in collection.find().sort("grades.0.score", -1).limit(3):
    print("- " + restaurant["name"] + " (Rating " + str(restaurant["grades"][0]["score"]) + ")")
