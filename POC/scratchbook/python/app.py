# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 00:12:18 2019

@author: user
"""
import service
import json

is_first = False
user_json = {"name":"Debrup","age":28,"gender":'M','avgBudget':1,'avgDuration':12,"tags":["outdoor","lake","pubs"]}
updated_json = {'user_id':'5ca69d6f6eef607efc321f5c','avgBudget':1,'avgDuration':6}
#5ca69a816eef607efc321f48
if(is_first):
    service.plan_trip(json.dumps(user_json))
else:
    service.plan_trip(json.dumps(updated_json))