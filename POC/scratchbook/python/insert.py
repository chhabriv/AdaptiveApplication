# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:20:43 2019

@author: user
"""
from mongoconnection import MongoConnection
from random import randint

def insertUser(name,age,gender,budget=0,duration=0,visited={},prefCategories=""):
    landmark=nature=shopping=theatre=restaurant = 0
    for aCat in  prefCategories.split(","):
        if(aCat == "landmark"):
            landmark = 1
        elif (aCat == "nature"):
            nature = 1
        elif (aCat == "shopping"):
            shopping = 1
        elif (aCat == "theatre"):
            theatre = 1
        else :
            restaurant = 1
    
    userId = randint(1000,9999)
    categories = {"landmark":landmark,"nature":nature,"shopping":shopping,"theatre":theatre,"restaurant":restaurant}
    userDetails = {"userId": userId,"name":name,"age":age,"gender":gender,"avgBudget":budget,"avgDuration":duration,"visited":visited, "categories":categories}
    
    conn = MongoConnection()
    print(conn.dummy())
    user_coll = conn.getUsersCollection()
    
    row = user_coll.insert_one(userDetails)
    print(row.inserted_id)
    if( row.acknowledged):
        return userId
    
    
def fetchUser(userId):
    query = {"userId":userId}
    
    conn = MongoConnection()
    
    user_coll = conn.getUsersCollection()
    row = user_coll.find_one(query)
    
    print (row)
    return row
    
    
def main():
    prefCat = "landmark,shopping,theatre"
    userId = insertUser("zihan",23,"F",0,0,{},prefCat)
    print(userId)
    userDtls = fetchUser(userId)
    if (userDtls):
        print(userDtls['gender'])    
    
    
main()
    