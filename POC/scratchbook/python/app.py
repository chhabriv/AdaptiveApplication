# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 00:12:18 2019

@author: user
"""
import service
import json

is_first = True
user_json = {"name":"Aneek","age":23,"gender":'M','avgBudget':"1",'avgDuration':"6","tags":["lakes","museum","pubs"]}
updated_json = {'user_id':'5ca69d6f6eef607efc321f5c','avgBudget':"1",'avgDuration':"6"}
updated_categories_json = {'user_id':'5ca69d6f6eef607efc321f5c','avgBudget':"1",'avgDuration':"6","tags":["lake"]}
#5ca69a816eef607efc321f48
if(is_first):
    a,b = service.plan_trip(json.dumps(user_json))
    print("user id",a)
    print("places",b)
else:
    service.plan_trip(json.dumps(updated_categories_json))
