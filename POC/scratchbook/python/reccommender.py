# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:29:34 2019

@author: user
"""
import user_crud as userService
import constants
import logging
from flask import current_app
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

PERSONAL_WEIGHT_FACTOR = 1.5

def contentFiltering(user,categories):
    catWeightsToUpdate = constants.CATEGORY_WEIGHT_STRUCT #{"landmark":0,"nature":0,"shopping":0,"restaurant":0,"theatre":0}
    current_app.logger.info('%s %s','input category weights -- ',categories)
    presentCategories = user["categories"]
    current_app.logger.info('%s %s','stored category weights -- ',presentCategories)
    #print(catWeights['nature'])
    for aCat in categories:
        #print(weights[aCat])
        presentWeight = presentCategories[aCat]
        #print(presentWeight)
        newWeight = categories[aCat]
        #if(newWeight == 0):
            #continue       
        #print(newWeight)
        updatedWeight = round((presentWeight + newWeight) / 2, 2)
        catWeightsToUpdate[aCat] = updatedWeight
        
    current_app.logger.info('%s %s','final category weights',catWeightsToUpdate)      
    return catWeightsToUpdate
        
        

    
    
def collaborativeFiltering(user):
    catWeights = constants.CATEGORY_WEIGHT_STRUCT #{"landmark":0,"nature":0,"shopping":0,"restaurant":0,"theatre":0}
    current_app.logger.info(user)
    presentCategories = user["categories"]
    avgWeights = userService.fetchCategoryWeightsForSimilarUsers(user['age'],user['gender'],user['avgBudget'],user['avgDuration'])
    current_app.logger.info('%s %S','similar user weights -- ',avgWeights)
    for aCat in presentCategories:
        #print(weights[aCat])
        presentWeight = presentCategories[aCat]
        #if(presentWeight == 0):
            #continue
        current_app.logger.info('%s %s',aCat,presentWeight)
        newWeight = avgWeights[0][aCat]
        current_app.logger.info('%s %s',aCat,newWeight)
        updatedWeight = round((presentWeight + newWeight) / 2, 2)
        catWeights[aCat] = updatedWeight
    current_app.logger.info('%s %s','final category weights',catWeights)    
    return catWeights


def collabFiltering(user_age,user_categories,user_gender,user_budget,user_duration):
    current_app.logger.info('Collab filtering invoked')
    catWeights = constants.CATEGORY_WEIGHT_STRUCT #{"landmark":0,"nature":0,"shopping":0,"restaurant":0,"theatre":0}
    #print(user)
    #presentCategories = user["categories"]
    current_app.logger.info('%s %s','user current weights -- ',user_categories)
    avgWeights = userService.fetchCategoryWeightsForSimilarUsers(user_age,user_gender,user_budget,user_duration)
    current_app.logger.info('%s %s','similar user weights -- ',avgWeights)
    for aCat in user_categories:
        #print(weights[aCat])
        presentWeight = user_categories[aCat]
        #current_app.logger.info('$s %s',aCat,str(presentWeight))
        #if(presentWeight == 0):
            #current_app.logger.info(aCat)
            #continue
        #current_app.logger.info('%s %s',aCat,presentWeight)
        newWeight = avgWeights[0][aCat]
        #current_app.logger.info('%s %s',aCat,str(newWeight))
        updatedWeight = round((presentWeight*PERSONAL_WEIGHT_FACTOR + newWeight) / 2, 2)
        catWeights[aCat] = updatedWeight
    current_app.logger.info('%s %s','final category weights',catWeights)        
    return catWeights


def main():
    user = userService.fetchUser(6216)
    #categories = {"theatre":2,"nature":1,"landmark":1,"shopping":0,"restaurant":0}
    #weightsToUpdate = contentFiltering(user,categories)
    avgWeights = collaborativeFiltering(user)
    print('curr user matching average weights -- ',avgWeights)
    
#main()
    
        