# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:36:45 2019

@author: user
"""
from pymongo import MongoClient

class MongoConnection():
    
    client = MongoClient('localhost', 27017)
    db = client["adaptive"]
    
    def getPlacesCollection(self):
        placeColl = MongoConnection.db['places']
        return placeColl
    
    def getUsersCollection(self):
        userColl = MongoConnection.db['users']
        return userColl
    
    def dummy(self):
        return "invoked"