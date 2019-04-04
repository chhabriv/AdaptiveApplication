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
import recommender
import places_crud

NAME='name'
GENDER='gender'
AGE='age'
BUDGET='budget'
TAGS='tags'
DURATION='duration'
IS_FIRST='is_first'
USER_ID='user_id'
CATEGORY='category'
USER_ID_CHECK=''
ID='_id'
OBJ_ID='$oid'

CATEGORY_TAG={'landmark': ['outdoor', 'museum','historic'],
     'nature': ['park', 'lake','outdoor'],
     'restaurant': ['food', 'pubs','historic'],
     'theater': ['play', 'movie','historic'],
     'shopping': ['styling', 'attire','shoes'] }

INITIAL_WEIGHT_DICT={'landmark': 0,
                     'nature': 0,
                     'restaurant': 0,
                     'theater': 0,
                     'shopping': 0 }

def plan_trip(user_json):
    user_received=json.loads(user_json)
    user_id=user_received[USER_ID]
    chosen_duration=user_received[DURATION]
    chosen_budget=user_received[BUDGET]
    if user_id is USER_ID_CHECK:
        user_object=process_input(user_received)
        user=json.loads(save_user(user_object))
    else:
        retrieved_user=json.loads(retrieve_user(user_id))
        if user_received[TAGS] is not '':
            current_category_weights=tags_to_category(user_received[TAGS])
            updated_weights=RECOMMENDER_CONTENT_FILTERING(retrieved_user,current_category_weights)
        else:
            updated_weights=RECOMMENDER_COLLAB_FILTERING(retrieved_user)
        update=update_user(user_id,updated_weights,chosen_duration,chosen_budget)
        if update==1:
            user=json.loads(retrieve_user(user_id))
        else:
            print("USER UPDATE WITH NEW WEIGHTS FAILED")
    category=user[CATEGORY]
    chosen_category=choose_category(category)
    raw_places=PLACES_CRUD_METHOD(chosen_category,chosen_budget)
    places_to_visit=preferred_places(raw_places,category,duration)
    return user[ID][OBJ_ID], places_to_visit
        
def process_input(user_received):
        if user_received[TAGS] is not '':
           category_weights= tags_to_category(user_received[TAGS])
        else:
            print("ERROR, NEW USER MUST HAVE TAGS")
        user_object=dto.user(
                            name=user_received[NAME],
                            age=user_received[AGE],
                            gender=user_received[GENDER],
                            budget=user_received[BUDGET],
                            category=category_weights,
                            duration=user_received[DURATION]
                        )
        return user_object
        
def tags_to_category(tags):
    weights=INITIAL_WEIGHT_DICT
    global TAGS
    
    for category in CATEGORY_TAG:
        for tag in tags:
            if tag in CATEGORY_TAG.get(category):
                weights[category]=weights[category]+1;
     
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
		available_duration = catWeights[aCat]/total_weight*duration*60
        print("the available duration for ",aCat," is ",available_duration)
        validLocations.extend(limitPlacesByCategoryDuration(raw_places,aCat,available_duration))
	return validLocations
        



def limitPlacesByCategoryDuration(locations,category_name,duration):
    validLocations= []
    currDuration = 0
    if(duration==currDuration):
        return validLocations
    #print(places.count())
    for aLoc in locations:
        #print(aLoc['name'],aLoc['duration'])
        if(aLoc['category']==category_name):
            if((currDuration + aLoc['duration']) <= duration):
                currDuration += aLoc['duration']
                data = aLoc['name'] +"--"+ str(aLoc['duration'])
                validLocations.append(data)
    print(validLocations)
    return validLocations 


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

update_user=dto.user.objects(id='5ca423beb3baf13518d185e6').update(
        duration=99,budget=50)



            
        
        
        