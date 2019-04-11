# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:23:46 2019

@author: viren
"""
from mongoengine import *
from mongoconnection import MongoConnection
import dto
import json
import user_crud
import reccommender
import places_crud
import logging
import random
from flask import current_app
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

NAME='name'
GENDER='gender'
AGE='age'
BUDGET='avgBudget'
TAGS='tags'
DURATION='avgDuration'
IS_FIRST='is_first'
USER_ID='user_id'
CATEGORY='categories'
USER_ID_CHECK=''
ID='_id'
OBJ_ID='$oid'

CATEGORY_TAG={'landmark': ['outdoor', 'museum','historic'],
     'nature': ['park', 'lake','outdoor'],
     'restaurant': ['food', 'pubs','historic'],
     'theatre': ['play', 'movie','historic'],
     'shopping': ['styling', 'attire','shoes'] }

INITIAL_WEIGHT_DICT={'landmark': 0,
                     'nature': 0,
                     'restaurant': 0,
                     'theatre': 0,
                     'shopping': 0 }

def plan_trip(user_json):
    current_app.logger.info("Starting to plan trip")
    current_app.logger.info(user_json)
    #print("invoked plan trip -- ",user_json)
    user_received=json.loads(user_json)
    user_id = ''
    if(USER_ID in user_received):
        user_id=user_received[USER_ID]
    chosen_duration=user_received[DURATION]
    chosen_budget=user_received[BUDGET]
    if user_id is USER_ID_CHECK:
        current_app.logger.info("Creating a new user and fetching places")
        #print('creating new user and fetching places')
        user_object=process_input(user_received)
        user=json.loads(save_user(user_object))
    else:
        retrieved_user=json.loads(retrieve_user(user_id))
        update_mongo=False
        if (user_received[TAGS]):
            current_app.logger.info('Tags present so content filtering')
            current_category_weights=tags_to_category(user_received[TAGS])
            updated_weights=reccommender.contentFiltering(retrieved_user,current_category_weights)
            update_mongo=True
        else:
            current_app.logger.info('No tags so collab filtering')
            updated_weights=reccommender.collabFiltering(retrieved_user[AGE],retrieved_user[CATEGORY],retrieved_user[GENDER],chosen_budget,chosen_duration,)
        current_app.logger.info(updated_weights)
        if update_mongo:
            update=update_user(user_id,updated_weights,chosen_duration,chosen_budget)
            if update==1:
                current_app.logger.info("User {} updated successfully".format(user_id))
            else:
                current_app.logger.info("User {} update failed".format(user_id))
        user=json.loads(retrieve_user(user_id))
        user[CATEGORY]=updated_weights
            #print("USER UPDATE WITH NEW WEIGHTS FAILED")
    current_app.logger.info(user[ID][OBJ_ID])        
    #current_app.logger.info(user[ID][OBJ_ID])
    category=user[CATEGORY]
    #print('user categories -- ',category)
    chosen_category=choose_category(category)
    #print('categories chosen -- ',chosen_category)
    raw_places=places_crud.fetchPlacesByCategoriesBudget(chosen_category,chosen_budget)
    #print('available places as per choice -- ',raw_places)
    places_to_visit=preferred_places(raw_places,category,chosen_duration)
    #print('recommended places -- ',places_to_visit)
    current_app.logger.info("Trip plannning completed")
    #print('trip planned')
    return user[ID][OBJ_ID],user[NAME], places_to_visit
        
def process_input(user_received):
        if user_received[TAGS] is not '':
           category_weights= tags_to_category(user_received[TAGS])
           current_app.logger.info(category_weights)
        else:
            print("ERROR, NEW USER MUST HAVE TAGS")
        user_object=None
        user_object=dto.user(
                            name=user_received[NAME],
                            age=user_received[AGE],
                            gender=user_received[GENDER],
                            avgBudget=user_received[BUDGET],
                            categories=category_weights,
                            avgDuration=user_received[DURATION]
                        )
        #print('user object model -- ',user_object)
        return user_object
        
def tags_to_category(tags):
    #print(tags)
    current_app.logger.info('%s %s','initial weights',INITIAL_WEIGHT_DICT)
    weights=''
    
    weights=INITIAL_WEIGHT_DICT.copy()
    #current_app.logger.info(weights)
    
    #global TAGS
    #print('tags -- ',tags)
    for category in CATEGORY_TAG:
        #print('category -- ',category)
        for tag in tags:
            #print('tag -- ',tag)
            #print('tag in category -- ',CATEGORY_TAG.get(category))
            if tag in CATEGORY_TAG.get(category):
                #print('matched -- ',tag,category)
                weights[category]=weights[category]+1;
    current_app.logger.info(weights)
    #print(weights)
    return weights
     
def choose_category(category_weights):
    chosen_categories=[]
    for category in category_weights:
        if category_weights.get(category) is not 0:
            chosen_categories.append(category)
    return chosen_categories

def save_user(user_object):
    return user_crud.insert_user(user_object).to_json()

def retrieve_user(user_id):
    return user_crud.retrieve_user(user_id).to_json()   

def update_user(user_id,updated_weights,chosen_duration,chosen_budget):
    return user_crud.update_user(user_id,updated_weights,chosen_duration,chosen_budget)
    
def preferred_places(raw_places,cat_weights,duration):
    validLocations = []
    total_weight = sum(cat_weights[cat] for cat in cat_weights)
    for aCat in cat_weights.keys():
        available_duration = cat_weights[aCat]/total_weight*int(duration)*60
        avlbl_duration_category = "the available duration for ",aCat," is ",available_duration
        current_app.logger.info(avlbl_duration_category)
        #print("the available duration for ",aCat," is ",available_duration)
        validLocations.extend(limitPlacesByCategoryDuration(raw_places,aCat,available_duration))
	
    return shuffleList(validLocations)
        



def limitPlacesByCategoryDuration(locations,category_name,duration):
    validLocations= []
    currDuration = 0
    if(duration==currDuration):
        return validLocations
    #print(places.count())
    for aLoc in locations:
        #print(aLoc['name'],aLoc['duration'])
        if(aLoc['category']==category_name):
            #print(aLoc['name'],aLoc['duration'])
            if((currDuration + aLoc['duration']) <= duration):
                currDuration += aLoc['duration']
                #data = aLoc['name'] +"--"+ str(aLoc['duration'])
                validLocations.append(aLoc)
    #print(validLocations)
    return validLocations 


def shuffleList(places):
    random.shuffle(places)
    return places
	
'''
#Testing code below
category_weights= tags_to_category(['shoes','movie','outdoor'])
user_test=user(
        name='sample5',
        age=26,
        gender='F',
        budget=0,
        category=category_weights,
        duration=6,
        is_first=True)

res=json.loads(user_crud.insert_user(user_test).to_json())

retrieved_user=user_crud.retrieve_user(res['id'])

#update_user=dto.user.objects(id='5ca423beb3baf13518d185e6').update(
 #       duration=99,budget=50)

'''

            
        
        
        