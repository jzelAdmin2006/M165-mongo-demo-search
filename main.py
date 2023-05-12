#!/usr/bin/python3

from pymongo import MongoClient

connectionString = "mongodb://localhost:27017/"
client = MongoClient(connectionString)
db = client["db_restaurant"]
restaurants = db["restaurants"]
print("Alle Stadtbezirke:")
for borough in restaurants.distinct("borough"):
    print("- " + borough)

print("Top 3 restaurants mit höchstem Rating:")
for restaurant in restaurants.find().sort("grades.0.score", -1).limit(3):
    print("- " + restaurant["name"] + " (Rating " + str(restaurant["grades"][0]["score"]) + ")")

le_perigord = restaurants.find_one({"name": "Le Perigord"})
print("Le Perigord:")
le_perigord_coord = le_perigord["address"]["coord"]
print(le_perigord_coord)

print("Restaurant, welches am nächsten zu Le Perigord liegt (Pythagoras):")
nearest_restaurant = None
nearest_restaurant_distance = None
for restaurant in restaurants.find({"$and": [{"address.coord": {"$ne": []}}, {"name": {"$ne": "Le Perigord"}}]}):
    restaurant_coord = restaurant["address"]["coord"]
    restaurant_distance = ((restaurant_coord[0] - le_perigord_coord[0]) ** 2 + (
            restaurant_coord[1] - le_perigord_coord[1]) ** 2) ** 0.5
    if nearest_restaurant is None or restaurant_distance < nearest_restaurant_distance:
        nearest_restaurant = restaurant
        nearest_restaurant_distance = restaurant_distance
print("- " + nearest_restaurant["name"] + " (" + str(nearest_restaurant_distance) + ")")
