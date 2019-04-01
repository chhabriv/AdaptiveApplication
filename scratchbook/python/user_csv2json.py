# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 00:43:25 2019

@author: user
"""

import csv, json

csvfile = open('..\\..\\..\\data\\bulk_user.csv', 'r')
jsonfile = open('..\\..\\..\\data\\user_bulk.json', 'w')

reader = csv.DictReader(csvfile)
arr = []
for row in reader:
    #print(row['userid'])
    #break
    data = {'userId' : row['userid'], 'name' : row['name'], 'gender':row['gender'], 'avgBudget' : row['avg spend'],'avgDuration' : row['duration'], 'categories':[{'name':'landmark','weight':int(row['landmark'])},{'name':'nature','weight':int(row['nature'])},{'name':'theatre','weight':int(row['theatre'])},{'name':'shopping','weight':int(row['shopping'])},{'name':'restaurant','weight':int(row['restaurant'])}]}
    #print (data)
    arr.append(data)
    #jsonfile.write('\n')
#json.dump(arr,jsonfile)
jsonfile.close()