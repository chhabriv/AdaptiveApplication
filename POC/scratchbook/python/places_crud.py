# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:11:12 2019

@author: user
"""

from mongoconnection import MongoConnection
import user_crud as user
import random 
import json


def fetchPlacesbyCategoriesDuration(categories,duration):
    catArr = categories.lower().split(",")
    inQry = { "category": { "$in": catArr } }
    
    dbConn = MongoConnection()
    places_coll = dbConn.getPlacesCollection()
    
    places = places_coll.find(inQry)
    
    locations = []
    validLocations= []
    currDuration = 0
    #print(places.count())
    if(places):
        for aPlace in places:
            locations.append(aPlace)
            
        shuffleList(locations)
        for aLoc in locations:
            print(aLoc['name'],aLoc['duration'])
            if((currDuration + aLoc['duration']) < duration):
                currDuration += aLoc['duration']
                validLocations.append(aLoc)
            else:
                break
            
        print(currDuration)
        
        print([aPlace['name'] for aPlace in validLocations])


def fetchPlacesByCategories(categories):
    
    inQry = { "category": { "$in": categories } }
    
    dbConn = MongoConnection()
    places_coll = dbConn.getPlacesCollection()
    
    places = places_coll.find(inQry)
    
    locations = []
    
    if(places):
        for aPlace in places:
            locations.append(aPlace)
    return shuffleList(locations)

def fetchPlacesByStoredCategories(categories):
    print(categories)
    catArr=categories
    inQry = { "category": { "$in": catArr } }
    print(inQry)
    dbConn = MongoConnection()
    places_coll = dbConn.getPlacesCollection()

    places = places_coll.find(inQry)
 
    locations = []
 
    if(places):
        for aPlace in places:
            locations.append(aPlace)
    return shuffleList(locations)
        
def shuffleList(places):
    random.shuffle(places)
    return places

def limitPlacesByCategories(locations,category,limit):
    #print('limit for category',category,"-",limit)
    currCount = 0
    validLocations = []
    for aLoc in locations:
        if(aLoc['category'] == category):
            if(currCount<limit):
                currCount += 1
                validLocations.append(aLoc)
                #print(aLoc['name'])
    #print([aLoc['name'] for aLoc in validLocations])    
    return validLocations



def fetchPlacesByCategoriesBudget(categories,budget):
    query = dict()
    query["category"] = { "$in": categories }
    query["Price"] = {"$lte":20}
    print(query)
    dbConn = MongoConnection()
    places_coll = dbConn.getPlacesCollection()
    
    places = places_coll.find(query)
    
    locations = []
    
    if(places):
        for aPlace in places:
            locations.append(aPlace)
    return shuffleList(locations)




def main():
    #fetchPlacesbyCategoriesDuration("landmark,nature",100)
    userId= 7883
    categories = ""
    userDtls = user.fetchUser(userId)
    if(not categories):
        #cat = userDtls["categories"]
        catWeights = userDtls["categories"]
        #print(cat.keys())
        locs = fetchPlacesByCategories(list(catWeights.keys()))
        validLocations1 = [];
        for aCat in catWeights.keys():
            #print(weights[aCat])
            validLocations1.extend(limitPlacesByCategories(locs,aCat,catWeights[aCat]))
        print("Locations to visit :",[{aLoc['name'],aLoc['category']} for aLoc in validLocations1])
    else:
        locations = fetchPlacesByCategories(categories.lower().split(","))
        validLocations2 = [];
        catWeightsToUpdate = {"landmark":0,"nature":0,"shopping":0,"restaurants":0,"theatre":0}
        for aCat in categories.lower().split(","):
            #print(weights[aCat])
            catWeightsToUpdate[aCat]=1
            validLocations2.extend(limitPlacesByCategories(locations,aCat,catWeights[aCat]+1))
        print("Locations to visit :",[{aLoc['name'],aLoc['category']} for aLoc in validLocations2])    
        #print(validLocations[0])
        print("Weights to update",catWeightsToUpdate)
        #user.updateWeightsByJson(userId,json.dumps(catWeightsToUpdate))
        
    
    
#main()
