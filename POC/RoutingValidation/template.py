import csv
import json
import requests

'''
NOTES

1. Provided LatLng doesnt always redirect to correct place. 
Should add an address/fullname column to dataset. 

2. Need to provide a start/end location and 1 waypoint. 
Should look into routing as follows;
origin      -> attraction best seen in morning 
waypoint    -> afternoon/late morning attraction 
destination -> evening attraction.


3. ToDo: Add more waypoints
    Starting place: attraction with latest opening hours
    Final place: attraction with earliest closing time 

'''


class Attraction:
    Category = ""
    Name = ""
    OpeningHours = 0
    ClosingHours = 0
    Latitude = 0
    Longitude = 0
    LatLng = 0
    Duration = 0

apiKey = 'AIzaSyB2NHLaqVDF0uSmuNBMXI3DVsUanzdRD7Q'
url = 'https://maps.googleapis.com/maps/api/directions/json'

def getRecommendedTimeSpent(object):
    return int(object['Duration'])


def getTotalDurationDistance(data, attractions):
    routes = data['routes']
    totalTravelTime = 0
    totalAttractionTime = 0
    for route in routes:
        legs = route['legs']
        for i in range(0, len(legs)):

            currentLeg = legs[i]
            currentTravelTime = round(int(currentLeg['duration']['value'])/60,2)
            totalTravelTime += round(currentTravelTime,2)

            currentAttraction = attractions[i]
            currentAttractionTime = int(currentAttraction['Duration'])
            totalAttractionTime += currentAttractionTime

            print(totalTravelTime)
            print(totalAttractionTime)

    nextAttraction = attractions[len(attractions)-1]
    nextAttractionTime = int(nextAttraction['Duration'])
    totalAttractionTime += nextAttractionTime

    print(totalTravelTime)
    print(totalAttractionTime)

attractions = []

with open('objects.csv', 'r') as objectsCsv:
    reader = csv.reader(objectsCsv)
    for row in reader:
        row = row[0].split('\t')
        attractions.append({
            'Category': row[1],
            'Name':row[2],
            'OpeningHours':row[3],
            'ClosingHours':row[4],
            'Latitude':row[5],
            'Longitude':row[6],
            'Duration':row[7],
            'LatLng':row[5]+","+row[6]
        })

routes = [attractions[0], attractions[1], attractions[2]]

params = {
    'origin': routes[0]['LatLng'],
    'destination': routes[1]['LatLng'],
    'key': apiKey,
    'travelMode':'transit',
    'waypoints': routes[2]['LatLng']
}

r = requests.get(url, params=params)
data = json.loads(r.text)
print(data)
getTotalDurationDistance(data, routes)
