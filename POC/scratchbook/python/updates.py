# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:56:17 2019

@author: user
"""

from pymongo import MongoClient
from bson import json_util




def main():
    mongoClient = MongoClient("mongodb://localhost:27017/")

    db = mongoClient["adaptive"]
    user_collection = db["users"]
    updateWeights(user_collection,9145,1,0,1,0,0)
    print(user_collection.find_one({"name":"zihan"}))
    

main()