# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 02:24:29 2019

@author: viren
"""
#mongod --dbpath "H:\TCD\Semester 2\AdaptiveApplications\Assignment-Main\Code\mongo-data"
from mongoengine import *
from mongoconnection import MongoConnection
import json

DBNAME='mongoengine_test'
connect(DBNAME)
    
class user(Document):
    name = StringField(required=True, max_length=15)
    age = IntField(required=True, max_length=2)
    gender = StringField(required=True, max_length=6)    
    budget = IntField(required=True, max_length=10)
    category = DictField(max_length=5)
    duration = IntField(required=True, max_length=10)
#    is_first= BooleanField(required=True, max_length=10)

# =============================================================================
# class category_weights(EmbeddedDocument):
#     landmark = IntField(required=True, max_length=10)
#     nature = IntField(required=True, max_length=10)
#     shopping = IntField(required=True, max_length=10)
#     restaurant = IntField(required=True, max_length=10)
#     theater = IntField(required=True, max_length=10)
# =============================================================================

class category(Document):
    category=StringField(required=True, max_length=15)
    tags=ListField(StringField(max_length=3))

#to put in another file


#User1.save()

print(user.name)

user2=User2.to_json()
user3=json.loads(user2)
user2
