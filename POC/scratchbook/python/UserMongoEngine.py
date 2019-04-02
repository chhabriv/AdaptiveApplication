# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 02:24:29 2019

@author: viren
"""
#mongod --dbpath "H:\TCD\Semester 2\AdaptiveApplications\Assignment-Main\Code\mongo-data"
from mongoengine import *
from mongoconnection import MongoConnection

connect('mongoengine_test', host='localhost', port=27017)
    
class user(Document):
    name = StringField(required=True, max_length=15)
    age = IntField(required=True, max_length=2)
    gender = StringField(required=True, max_length=6)    
    budget = IntField(required=True, max_length=10)
    tags = ListField(StringField(max_length=10))
    is_first= BooleanField(required=True, max_length=10)


User1=user(
        name="Viren",
        age=26,
        gender="Male",
        budget=0,
        tags=["shop","eat","drink"],
        is_first=True)

User1.save()

print(user.name)

User2=user.objects.first()