# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:24:00 2019

@author: user
"""

from pymongo import MongoClient
from bson import json_util

mongoClient = MongoClient("mongodb://localhost:27017/")

db = mongoClient["adaptive"]

print("Existing databases :",mongoClient.list_database_names())

dbList = mongoClient.list_database_names()

if "adapative" in dbList:
  print("The database exists.")
  
collection = db["places1"]

#print(db.list_collection_names())

collections = db.list_collection_names()

if "places" in collections:
  print("The collection exists.")
  
first_place = { "name": "Spire", "category": "Landmark" , "hours":{"opening":0000,"closing":2359},"geoLocation":{"latitude":"53.350027","longitude":"-6.260255"},"duration":15,"bestTimeToVisit":{"day":"evening","season":"summer"},"wayToGetThere":{"Best":"Walk","Suggested":"Walking"},"price":"low","suitableAge":"all"}
second_place = { "name": "Spire", "category": "Landmark" , "hours":{"opening":0000,"closing":2359},"geoLocation":{"latitude":"53.350027","longitude":"-6.260255"},"duration":30,"bestTimeToVisit":{"day":"morning","season":"autumn"},"wayToGetThere":{"Best":"Walk","Suggested":"Walking"},"price":"low","suitableAge":"all"}


#places_json_str = '''[{"place": {"Category": "Landmark", "Name": "Spire", "Hours": {"Opening": "0000", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.350027", "Longitude": "-6.260255"}, "Duration": "15", "Best Time to Visit": {"Day": "Evening", "Season": "Summer"}, "Review": "4.1", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Landmark", "Name": "Trinity College", "Hours": {"Opening": "0900", "Closing": "1700"}, "GeoLocation": {"Latitude": "53.343986", "Longitude": "-6.254572"}, "Duration": "90", "Best Time to Visit": {"Day": "Morning", "Season": "Summer"}, "Review": "4.5", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "14", "Suitable Age": "All"}}, {"place": {"Category": "Landmark", "Name": "Kilmainham Gaol", "Hours": {"Opening": "0930", "Closing": "1800"}, "GeoLocation": {"Latitude": "53.342062", "Longitude": "-6.309794"}, "Duration": "90", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.5", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "8", "Suitable Age": "All"}}, {"place": {"Category": "Landmark", "Name": "Temple Bar Area", "Hours": {"Opening": "0000", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.345253", "Longitude": "-6.267448"}, "Duration": "60", "Best Time to Visit": {"Day": "Night", "Season": "Summer"}, "Review": "4.5", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "0", "Suitable Age": "Adult"}}, {"place": {"Category": "Landmark", "Name": "Molly Malone Statue", "Hours": {"Opening": "0000", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.343808", "Longitude": "-6.260992"}, "Duration": "10", "Best Time to Visit": {"Day": "Morning", "Season": "Summer"}, "Review": "", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Landmark", "Name": "Samuel Beckett Bridge", "Hours": {"Opening": "0000", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.347109", "Longitude": "-6.241403"}, "Duration": "15", "Best Time to Visit": {"Day": "Evening", "Season": "Summer"}, "Review": "4.6", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Landmark", "Name": "The Custom House", "Hours": {"Opening": "0900", "Closing": "1700"}, "GeoLocation": {"Latitude": "53.348877", "Longitude": "-6.253128"}, "Duration": "30", "Best Time to Visit": {"Day": "Morning", "Season": "Winter"}, "Review": "4.4", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "1", "Suitable Age": "All"}}, {"place": {"Category": "Landmark", "Name": "Ha'penny Bridge", "Hours": {"Opening": "0000", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.346483", "Longitude": "-6.263119"}, "Duration": "15", "Best Time to Visit": {"Day": "Evening", "Season": "Summer"}, "Review": "4.4", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Landmark", "Name": "Aviva Stadium", "Hours": {"Opening": "1000", "Closing": "1500"}, "GeoLocation": {"Latitude": "53.335386", "Longitude": "-6.228403"}, "Duration": "75", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.6", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "10", "Suitable Age": "All"}}, {"place": {"Category": "Landmark", "Name": "Poolbeg Lighthouse", "Hours": {"Opening": "0000", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.342317", "Longitude": "-6.151346"}, "Duration": "90", "Best Time to Visit": {"Day": "Evening", "Season": "Summer"}, "Review": "4.7", "Way to get there": {"Best": "Car", "Suggested": "Car"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Nature/Park", "Name": "St. Stephen's Green", "Hours": {"Opening": "0800", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.3382", "Longitude": "-6.2591"}, "Duration": "30", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.8", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Nature/Park", "Name": "Phoenix Park", "Hours": {"Opening": "0800", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.3559", "Longitude": "-6.3298"}, "Duration": "60", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.3", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Nature/Park", "Name": "Merrion Square", "Hours": {"Opening": "0800", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.3396", "Longitude": "-6.249"}, "Duration": "15", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.1", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Nature/Park", "Name": "Irish National War Memorial Gardens", "Hours": {"Opening": "0800", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.3456", "Longitude": "-6.3135"}, "Duration": "30", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.9", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Nature/Park", "Name": "National Botanic Gardens", "Hours": {"Opening": "1000", "Closing": "1630"}, "GeoLocation": {"Latitude": "53.3725", "Longitude": "-6.2719"}, "Duration": "45", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.8", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Nature/Park", "Name": "Sandymount Green", "Hours": {"Opening": "0800", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.34138972", "Longitude": "-6.2219696"}, "Duration": "60", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.6", "Way to get there": {"Best": "Walk", "Suggested": "Walk"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Nature/Park", "Name": "Ticknock Hill", "Hours": {"Opening": "0800", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.25954502", "Longitude": "-6.255942198"}, "Duration": "300", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.5", "Way to get there": {"Best": "Car", "Suggested": "Car"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Nature/Park", "Name": "Dublin Zoo", "Hours": {"Opening": "0930", "Closing": "1800"}, "GeoLocation": {"Latitude": "53.3562", "Longitude": "-6.3053"}, "Duration": "120", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.1", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "19.5", "Suitable Age": "All"}}, {"place": {"Category": "Nature/Park", "Name": "Howth", "Hours": {"Opening": "0800", "Closing": "2359"}, "GeoLocation": {"Latitude": "53.3786", "Longitude": "-6.057"}, "Duration": "300", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "4.6", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "0", "Suitable Age": "All"}}, {"place": {"Category": "Nature/Park", "Name": "SEA Life Bray", "Hours": {"Opening": "", "Closing": "1800"}, "GeoLocation": {"Latitude": "53.2034", "Longitude": "-6.0982"}, "Duration": "90", "Best Time to Visit": {"Day": "Afternoon", "Season": "Summer"}, "Review": "3.5", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "25", "Suitable Age": "All"}}, {"place": {"Category": "Shopping", "Name": "Stephen's Green Shopping Centre", "Hours": {"Opening": "0900", "Closing": "1900"}, "GeoLocation": {"Latitude": "53.34014", "Longitude": "-6.261419"}, "Duration": "", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "4.1", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": "All"}}, {"place": {"Category": "Shopping", "Name": "Powerscourt Centre", "Hours": {"Opening": "1000", "Closing": "1800"}, "GeoLocation": {"Latitude": "53.342141", "Longitude": "-6.261221"}, "Duration": "", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "4.3", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": "All"}}, {"place": {"Category": "Shopping", "Name": "Jervis Shopping Centre", "Hours": {"Opening": "0900", "Closing": "1830"}, "GeoLocation": {"Latitude": "53.348541", "Longitude": "-6.265215"}, "Duration": "", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "4.2", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": "All"}}, {"place": {"Category": "Shopping", "Name": "George's Street Arcade", "Hours": {"Opening": "0900", "Closing": "1830"}, "GeoLocation": {"Latitude": "53.342483", "Longitude": "-6.263913"}, "Duration": "", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "4.2", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": "All"}}, {"place": {"Category": "Shopping", "Name": "Royal Hibernian Way Shopping Centre", "Hours": {"Opening": "0800", "Closing": "1800"}, "GeoLocation": {"Latitude": "53.341355", "Longitude": "-6.258368"}, "Duration": "", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "4.4", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": "All"}}, {"place": {"Category": "Shopping", "Name": "Ilac Shopping Centre", "Hours": {"Opening": "0900", "Closing": "1830"}, "GeoLocation": {"Latitude": "53.350405", "Longitude": "-6.262796"}, "Duration": "", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "4", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": "All"}}, {"place": {"Category": "Shopping", "Name": "The Westbury Mall", "Hours": {"Opening": "0800", "Closing": "1800"}, "GeoLocation": {"Latitude": "53.341664", "Longitude": "-6.260692"}, "Duration": "", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "4.3", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": "All"}}, {"place": {"Category": "Shopping", "Name": "Moore Street Shopping Mall", "Hours": {"Opening": "1000", "Closing": "1900"}, "GeoLocation": {"Latitude": "53.351385", "Longitude": "-6.262978"}, "Duration": "", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "3.9", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": "All"}}, {"place": {"Category": "Shopping", "Name": "Point Square Dublin", "Hours": {"Opening": "0800", "Closing": "2300"}, "GeoLocation": {"Latitude": "53.348365", "Longitude": "-6.228373"}, "Duration": "", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "4", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": "All"}}, {"place": {"Category": "Shopping", "Name": "Swan Shopping Center", "Hours": {"Opening": "0900", "Closing": "2100"}, "GeoLocation": {"Latitude": "53.323137", "Longitude": "-6.264928"}, "Duration": "", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "3.9", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": "All"}}, {"place": {"Category": "Theatres/Movies", "Name": "Bord G\u00c3\u00a1is Energy Theatre", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "53.344201", "Longitude": "-6.240274"}, "Duration": "", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.6", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "Varies", "Suitable Age": "Varies"}}, {"place": {"Category": "Theatres/Movies", "Name": "3Arena", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "53.347512", "Longitude": "-6.228482"}, "Duration": "", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.5", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "Varies", "Suitable Age": "Varies"}}, {"place": {"Category": "Theatres/Movies", "Name": "The Academy", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "53.34805", "Longitude": "-6.261853"}, "Duration": "", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.2", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "Varies", "Suitable Age": "Varies"}}, {"place": {"Category": "Theatres/Movies", "Name": "Olympia Theatre", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "53.344318", "Longitude": "-6.266114"}, "Duration": "", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.5", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "Varies", "Suitable Age": "Varies"}}, {"place": {"Category": "Theatres/Movies", "Name": "The Abbey Theatre Dublin", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "53.34854", "Longitude": "-6.257107"}, "Duration": "", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.7", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "Varies", "Suitable Age": "Varies"}}, {"place": {"Category": "Theatres/Movies", "Name": "Gaiety Theatre", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "53.340453", "Longitude": "-6.261572"}, "Duration": "", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.5", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "Varies", "Suitable Age": "Varies"}}, {"place": {"Category": "Theatres/Movies", "Name": "Liberty Hall Theatre", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "53.349805", "Longitude": "-6.26031"}, "Duration": "", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.3", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "Varies", "Suitable Age": "Varies"}}, {"place": {"Category": "Theatres/Movies", "Name": "Ambassador Theatre", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "53.352809", "Longitude": "-6.261987"}, "Duration": "", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "Varies", "Suitable Age": "Varies"}}, {"place": {"Category": "Theatres/Movies", "Name": "National Concert Hall", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "53.334718", "Longitude": "-6.259216"}, "Duration": "", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.6", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "Varies", "Suitable Age": "Varies"}}, {"place": {"Category": "Brewery", "Name": "Guiness Storehouse", "Hours": {"Opening": "0930", "Closing": "1700"}, "GeoLocation": {"Latitude": "53.3419", "Longitude": "6.2867"}, "Duration": "90", "Best Time to Visit": {"Day": "Afternoon", "Season": "All"}, "Review": "4.5", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "18.50 +", "Suitable Age": "All"}}, {"place": {"Category": "Distillery ", "Name": "Jameson Distillery Bow St.", "Hours": {"Opening": "1000", "Closing": "1730"}, "GeoLocation": {"Latitude": "53.3484", "Longitude": "6.2774"}, "Duration": "40", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.5", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "18+", "Suitable Age": "All"}}, {"place": {"Category": "Restaurant", "Name": "Restaurant Patrick Guilbad", "Hours": {"Opening": "1230/1900", "Closing": "1400/2200"}, "GeoLocation": {"Latitude": "53.3384", "Longitude": "6.253"}, "Duration": "120", "Best Time to Visit": {"Day": "Evening", "Season": "All"}, "Review": "4.5", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "100-200", "Suitable Age": "All"}}, {"place": {"Category": "Restaurant", "Name": "Chai Yo", "Hours": {"Opening": "1230/1730", "Closing": "1500/0000"}, "GeoLocation": {"Latitude": "53.3357", "Longitude": "6.2478"}, "Duration": "90", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.5", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "50", "Suitable Age": "All"}}, {"place": {"Category": "Quick Bite", "Name": "Mamas Revenge", "Hours": {"Opening": "1000", "Closing": "2000"}, "GeoLocation": {"Latitude": "53.3419", "Longitude": "6.2538"}, "Duration": "60", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.5", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "20", "Suitable Age": "All"}}, {"place": {"Category": "Cafe", "Name": "The Vintage Teapot", "Hours": {"Opening": "0930", "Closing": "2000"}, "GeoLocation": {"Latitude": "53.3504", "Longitude": "6.2597"}, "Duration": "60", "Best Time to Visit": {"Day": "All", "Season": "All"}, "Review": "4.5", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "10+", "Suitable Age": "All"}}, {"place": {"Category": "", "Name": "", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "", "Longitude": ""}, "Duration": "", "Best Time to Visit": {"Day": "", "Season": ""}, "Review": "", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "", "Suitable Age": ""}}, {"place": {"Category": "", "Name": "", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "", "Longitude": ""}, "Duration": "", "Best Time to Visit": {"Day": "", "Season": ""}, "Review": "", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "", "Suitable Age": ""}}, {"place": {"Category": "", "Name": "", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "", "Longitude": ""}, "Duration": "", "Best Time to Visit": {"Day": "", "Season": ""}, "Review": "", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "", "Suitable Age": ""}}, {"place": {"Category": "", "Name": "", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "", "Longitude": ""}, "Duration": "", "Best Time to Visit": {"Day": "", "Season": ""}, "Review": "", "Way to get there": {"Best": "Public Transportation", "Suggested": "Public Transportation"}, "Price": "", "Suitable Age": ""}}, {"place": {"Category": "", "Name": "", "Hours": {"Opening": "", "Closing": ""}, "GeoLocation": {"Latitude": "", "Longitude": ""}, "Duration": "", "Best Time to Visit": {"Day": "", "Season": ""}, "Review": "", "Way to get there": {"Best": "", "Suggested": ""}, "Price": "", "Suitable Age": ""}}]'''
#row = collection.insert_one(first_place)

#places_json = json.loads()
#print(places_json[0]["place"]["Category"])

with open("D:\debrup\scratchbook\python\code\standalone\struct_v2.json") as json_file:
    place_data = json_util.loads(json_file.read())

print(place_data[0]["geoLocation"]["longitude"],",",place_data[0]["geoLocation"]["latitude"])

for aObj in place_data:
    geoObjType="Point"
    coordinates = [aObj["geoLocation"]["longitude"],aObj["geoLocation"]["latitude"]]
    print(coordinates)
    aObj["location"] = {"type":geoObjType,"coordinates":coordinates}
    if aObj["category"] == "nature/park":
        aObj["category"] = "nature"

print(place_data[10])
rows = collection.insert_many(place_data)

print(rows.inserted_ids)

print(collection.find().count())

print(collection.find_one({"bestTimeToVisit.season":"winter"}))

print(collection.count_documents())



user_collection = db["users"]

user1 = {"name":"Debrup","age":28,"gender":"M","avgBudget":0,"avgDuration":0,"visited":[]}
user2 = {"name":"Viren","age":26,"gender":"M","avgBudget":0,"avgDuration":0,"visited":[]}


row = user_collection.insert_one(user2)

print(row.inserted_id)

print(user_collection.find_one())

print(user_collection.find({"age":26})[0])

cat_pref_user1 = {"categories":[{"name":"landmark", "weight":1},{"name":"outdoor", "weight":1},{"name":"pubs", "weight":1},{"name":"theatre", "weight":1},{"name":"shopping", "weight":1}]}

cat_pref_user2 = {"categories":{"landmark":1,"resto":1,"theatre":1,"shopping":1,"nature":1}}

user_collection.update_one({"name":"Viren"},{"$set":cat_pref_user2})

user_collection.update_one({"name":"Viren"},{"$inc":{"categories.landmark":1}})

print(user_collection.find_one())

#db.places.find({$and:[{location:{$near:{$geometry:{type:"Point",coordinates:[-6.25313, 53.34888]}}}},{"_id":{$ne : ObjectId("5c9834696eef601f34a6e48f")}}]}).limit(2).pretty()

#db.places.find({$and:[{location:{$near:{$geometry:{type:"Point",coordinates:[-6.25313, 53.34888]}}}},{"location.coordinates":{$nin:[-6.25313,53.34888]}}]}).limit(2).pretty()


def insert_bulk_user():
    with open("D:\debrup\TCD\Adaptive_Application\data\user_bulk.json") as json_file:
        place_data = json_util.loads(json_file.read())
    
    
    mongoClient = MongoClient("mongodb://localhost:27017/")

    db = mongoClient["adaptive"]
    
      
    collection = db["user_dummy"]
    
    rows = collection.insert_many(place_data)
    
    print(rows.acknowledged)
    
    #print(rows.)

insert_bulk_user()