# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:49:54 2019

@author: user
"""

import argparse
import user_crud as user
import places_crud as place
import json

def main():
    name = "nicky"
    age = 25
    gender = "M"
    categories = "theatre,shopping,landmark"
    
    userId = user.insertUser(name,age,gender,0,0,{},categories)
    print(userId)
    userDtls = user.fetchUser(userId)
    
    cat = userDtls["categories"]
    #print(cat.keys())
    locs = place.fetchPlacesByCategories(list(cat.keys()))
    validLocations1 = [];
    for aCat in cat.keys():
        #print(weights[aCat])
        validLocations1.extend(place.limitPlacesByCategories(locs,aCat,cat[aCat]))
    print("Locations to visit :",[{aLoc['name'],aLoc['category']} for aLoc in validLocations1])
    
    categories = "nature,landmark"
    
    locations = place.fetchPlacesByCategories(categories.lower().split(","))
    validLocations2 = [];
    catWeightsToUpdate = {"landmark":0,"nature":0,"shopping":0,"restaurant":0,"theatre":0}
    for aCat in categories.lower().split(","):
        #print(weights[aCat])
        catWeightsToUpdate[aCat]=1
        validLocations2.extend(place.limitPlacesByCategories(locations,aCat,cat[aCat]+1))
    print("Locations to visit :",[{aLoc['name'],aLoc['category']} for aLoc in validLocations2])    
    #print(validLocations[0])
    print("Weights to update",catWeightsToUpdate)
    if(user.updateWeightsByJson(userId,json.dumps(catWeightsToUpdate))):
        print("Category weights for the user have been updated")


main()

    