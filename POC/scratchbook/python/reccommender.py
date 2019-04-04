# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:29:34 2019

@author: user
"""
import json
import user_crud as userService
import constants

def contentFiltering(user,categories):
    catWeightsToUpdate = constants.CATEGORY_WEIGHT_STRUCT #{"landmark":0,"nature":0,"shopping":0,"restaurant":0,"theatre":0}
    print('input category weights -- ',categories)
    presentCategories = user["categories"]
    print('stored category weights -- ',presentCategories)
    #print(catWeights['nature'])
    for aCat in categories:
        #print(weights[aCat])
        presentWeight = presentCategories[aCat]
        #print(presentWeight)
        newWeight = categories[aCat]
        if(newWeight == 0):
            continue
        
        #print(newWeight)
        updatedWeight = round((presentWeight + newWeight) / 2, 2)
        catWeightsToUpdate[aCat] = updatedWeight
        
        
    return catWeightsToUpdate
        
        

    
    
    
    
    

    
def collaborativeFiltering(user):
    catWeights = constants.CATEGORY_WEIGHT_STRUCT #{"landmark":0,"nature":0,"shopping":0,"restaurant":0,"theatre":0}
    presentCategories = user["categories"]
    avgWeights = userService.fetchCategoryWeightsForSimilarUsers(user['age'],user['gender'],user['avgBudget'],user['avgDuration'])
    print('similar user weights -- ',avgWeights)
    for aCat in presentCategories:
        #print(weights[aCat])
        presentWeight = presentCategories[aCat]
        if(presentWeight == 0):
            continue
        print(presentWeight)
        newWeight = avgWeights[0][aCat]
        print(newWeight)
        updatedWeight = round((presentWeight + newWeight) / 2, 2)
        catWeights[aCat] = updatedWeight
        
    return catWeights



def main():
    user = userService.fetchUser(6216)
    #categories = {"theatre":2,"nature":1,"landmark":1,"shopping":0,"restaurant":0}
    #weightsToUpdate = contentFiltering(user,categories)
    avgWeights = collaborativeFiltering(user)
    print('curr user matching average weights -- ',avgWeights)
    
main()
    
        