import pandas as pd
from pymongo import MongoClient

print("Creatting a connection to the dabase.")
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
print("Databases available:", client.list_database_names())
print(client)
db = client["test"]
print(db)
collection = db["users"]
print(collection)
# Retrieve and load data into DataFrame
data = list(collection.find())
df = pd.DataFrame(data) #.drop(columns=['_id'])

print(df)

vidCollection = db["videos"]
data = list (vidCollection.find())
df = pd.DataFrame(data).drop(columns=['_id'])
print(df)


