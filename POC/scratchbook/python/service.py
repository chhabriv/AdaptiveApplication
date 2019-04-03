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

CATEGORY_TAG={'landmark': ['outdoor', 'museum','historic'],
     'nature': ['park', 'lake','outdoor'],
     'restaurant': ['food', 'pubs','historic'],
     'theater': ['play', 'movie','historic'],
     'shopping': ['styling', 'attire','shoes'] }

def plan_trip(user_json):
    user_received=json.loads(user_json)
    if user_received[USER_ID] is '':
        saved_user=process_input(user_received,False)
        saved_user_json=saved_user.to_json()
        category_weight=saved_user[CATEGORY]
        chosen_category=choose_category(category_weight)
        chosen_budget=saved_user[BUDGET]
        duration=saved_user[DURATION]
        raw_places=PLACES_CRUD_METHOD(chosen_category,chosen_budget)
        places_to_visit=preferred_places(raw_places,category_weight,duration)
        return places_to_visit
    else:
        retrieve_user,current_category_weights=process_input(user_received,True)
        category_weight=retrieve_user[CATEGORY]
        chosen_category=choose_category(category_weight)
        duration=user_received[DURATION]
        chosen_budget=user_received[BUDGET]
        updated_weights=RECOMMENDER_CONTENT_FILTERING(category_weight,current_category_weights)
        updated_user=USER_CRUD(retrieve_user,updated_weights,duration,budget)
        raw_places=PLACES_CRUD_METHOD(chosen_category,chosen_budget)
        places_to_visit=preferred_places(raw_places,category_weight,duration)
        return places_to_visit
        
        
def process_input(user_received, is_exists):
    #setting required user input values to create an object
    if is_exists is False:
        if user_received[TAGS] is not '':
           category_weights= tags_to_category(user_received[TAGS])
        else:
            print("ERROR, NEW USER MUST HAVE TAGS")
        user_object=user(
                            name=user_received[NAME],
                            age=user_received[AGE],
                            gender=user_received[GENDER],
                            budget=user_received[BUDGET],
                            category=category_weights,
                            duration=user_received[DURATION],
                            is_first=user_received[IS_FIRST])
        saved_user=user_object.save()
        return saved_user
    else:
        user_id=user_received[USER_ID]
        retrieve_user=user_crud(user_id)#WRITE FUNCTION IN USER_CRUD
        if user_received[TAGS] is not '':
           category_weights= tags_to_category(user_received[TAGS])
           return retrieve_user,category_weights
        
def tags_to_category(tags):
    weights={'landmark': 0,'nature': 0,'restaurant': 0,'theater': 0,'shopping': 0 }
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
    print(chosen_categories)
    return chosen_categories

def preferred_places(raw_places,weights,duration):
    recommended=[]
    
    
    return recommended

category_weights= tags_to_category(['shoes','movie','historic'])
user_test=user(
        name='rupdeb',
        age=26,
        gender='F',
        budget=0,
        category=category_weights,
        is_first=True)

res=user_crud.insert_user(user_test)
str(res.category.landmark)

            
        
        
        