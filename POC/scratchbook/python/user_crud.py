# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:20:43 2019

@author: user
"""

from mongoconnection import MongoConnection
from random import randint
import json
import dto

def insert_user(user):
    return user.save()

def retrieve_user(user_id):
    return dto.user.objects.get(id=user_id)

def update_user(user_id,weight,new_budget,new_duration):
    return dto.user.objects(id=user_id).update(
            category=weight,
            duration=new_duration,
            budget=new_budget)

def insertUser(name,age,gender,budget=0,duration=0,visited={},prefCategories=""):
    landmark=nature=shopping=theatre=restaurant = 0
    
    for aCat in  prefCategories.split(","):
        #print(aCat)
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
    
    '''print("landmark",landmark)
    print("nature",nature)
    print("shopping",shopping)
    print("theatre",theatre)
    print("restaurant",restaurant)'''
    
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
    
    #print (row)
    return row
    
def updateWeights(userId,landmarkWeight, natureWeight, shopWeight, theatreWeight, restoWeight):
    print("categories.landmark",landmarkWeight,"categories.natureWeight",natureWeight,"categories.shopWeight",shopWeight, "categories.theatreWeight",theatreWeight,"categories.restoWeight",restoWeight)
    incStr = {"$inc":{"categories.landmark":landmarkWeight,"categories.nature":natureWeight,"categories.shopping":shopWeight, "categories.theatre":theatreWeight,"categories.restaurant":restoWeight}}
    conn = MongoConnection()
    user_coll = conn.getUsersCollection()
    user_coll.update_one({"userId":userId},incStr)

def updateWeightsByJson(userId,categoryWeights):
    print("invoked")
    catWeights = json.loads(categoryWeights)
    #print(catWeights['nature'])
    incStr = {"$inc":{"categories.landmark":catWeights['landmark'],
                      "categories.nature":catWeights['nature'],
                      "categories.shopping":catWeights['shopping'], 
                      "categories.theatre":catWeights['theatre'],
                      "categories.restaurant":catWeights['restaurant']}}
    #incStr = '''{"$inc":{"'''
    #for key,value in catWeights.items():
        #print (key,value)
        #incStr += "categories."+key+":"+value
    
    #incStr +='''}'''
    #print(incStr)
    conn = MongoConnection()
    user_coll = conn.getUsersCollection()
    row = user_coll.update_one({"userId":userId},incStr) 
    if(row.acknowledged):
        print("Weights updated successfully")
    return row.acknowledged
    


def fetchCategoryWeightsForSimilarUsers(age,gender,avgBudget,avgDuration):
    age = 60
    avgBudget = '2'
    avgDuration = '6'
    gender = 'M'


    match_query = {"$match":{"age":{"$gte":age-5,"$lte":age+5},"gender":gender,
                             "avgBudget":avgBudget,"avgDuration":avgDuration}}
    group_query = {"$group":{"_id":0,"landmark":{"$avg":"$categories.landmark"},
                             "nature":{"$avg":"$categories.nature"},
                             "restaurant":{"$avg":"$categories.restaurant"},
                             "shopping":{"$avg":"$categories.shopping"},
                             "theatre":{"$avg":"$categories.theatre"}}}
    project_query = {"$project":{"_id":0,"landmark":{"$ceil":"$landmark"},
                             "nature":{"$ceil":"$nature"},
                             "restaurant":{"$ceil":"$restaurant"},
                             "shopping":{"$ceil":"$shopping"},
                             "theatre":{"$ceil":"$theatre"}}}
    pipeline = [match_query,group_query]
    print(pipeline)
    conn = MongoConnection()
    #sprint(aColl for aColl in conn.db.list_collections())
    user_coll = conn.db['uers_dummy']
    row = user_coll.aggregate(pipeline)
    val = list(row)
    print(val)
    return val



def main():
    prefCat = "restaurant,nature,theatre"
    userId = insertUser("aneek",26,"M",0,0,{},prefCat)
    print(userId)
    userDtls = fetchUser(userId)
    cat = {'landmark': 0, 'nature': 1, 'shopping': 1, 'restaurant': 0, 'theatre': 0}
    #print(updateWeightsByJson(userId,json.dumps(cat)))
    #if (userDtls):
        #print(userDtls['gender'])    
    
    
#main()
    