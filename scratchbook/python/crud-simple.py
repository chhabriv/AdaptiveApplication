# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 00:59:14 2019

@author: Debrup
"""

##Install pymongo library sing pip or conda
from pymongo import MongoClient

#connect to the mongo server
mongoClient = MongoClient("mongodb://localhost:27017/")

#choose the database
db = mongoClient["test_db"]

print(mongoClient.list_database_names())

dbList = mongoClient.list_database_names()
if "test_db" in dbList:
  print("The database exists.")
  
#choose the collection
collection = db["test"]

print(db.list_collection_names())

collections = db.list_collection_names()
if "test" in collections:
  print("The collection exists.")
  
single = { "name": "Debrup", "address": "India" }

row = collection.insert_one(single)

print(row.inserted_id)

multiple = [
  { "name": "Viren", "address": "India"},
  { "name": "Sridhar", "address": "India"},
  { "name": "Zihan", "address": "China"},
  { "name": "Nicky", "address": "Malta"},
  { "name": "Ashwin", "address": "India"}
]

rows = collection.insert_many(multiple)

print(rows.inserted_ids)


fetchOne = collection.find_one()

print(fetchOne)

for aUser in collection.find():
    print (aUser)

for aUser in collection.find({},{"address"}):
    print (aUser) 


query = { "address": "China" }

for aUser in collection.find(query):
    print(aUser)
  
equalQry = { "address": { "$eq": "China" } }

notEqualQry = { "address": { "$ne": "China" } }

inQry = { "address": { "$in": ["China","Malta"] } }

ninQry = { "address": { "$nin": ["China","Malta"] } }

orQry = {"$or" : [{ "address": "China" }, {"name" : "Nicky"} ]}

andQry = {"$or" : [{ "address": "China" }, {"name" : "Zihan"} ]}

#notQry1 = { "address": { "$not": "China" }}

notQry2 = { "address": { "$not": {"$eq":"China" } }}

norQry = {"$nor" : [{ "address": "China" }, {"name" : "Nicky"} ]}

for aUser in collection.find(equalQry):
    print(aUser)
    
for aUser in collection.find(notEqualQry):
    print(aUser)

for aUser in collection.find(notQry2):
    print(aUser)

for aUser in collection.find(inQry):
    print(aUser)

for aUser in collection.find(ninQry):
    print(aUser)
    
for aUser in collection.find(orQry):
    print(aUser)
    
for aUser in collection.find(andQry):
    print(aUser)
    
for aUser in collection.find(notQry2):
    print(aUser)
    
for aUser in collection.find(norQry):
    print(aUser)
    

names = collection.find().sort("name")

for aName in names:
  print(aName)
  
names = collection.find().sort("name",-1)

for aName in names:
  print(aName)

upQry = {"$set":{"strand":"Inteligent Systems"}}

collection.update_one(query,upQry)

for aUser in collection.find(query):
    print(aUser)
    
manyUpQry = {"$set":{"strand":"Data Science"}}

collection.update_many({"address":"India"},manyUpQry)

for aUser in collection.find():
    print(aUser)

deleteOne = collection.delete_one(query)

print("is the record deleted ?",deleteOne.acknowledged)


deleteMany = collection.delete_many({})

print("Number of records deleted ?",deleteMany.deleted_count)

collection.drop()

print(db.list_collection_names())