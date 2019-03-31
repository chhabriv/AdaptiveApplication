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


3. Done: Add more waypoints -> seems like in python only can add one waypoint (from my research)
                            -> separate the trip as multiple ones with three points each and add up the duration plus transit
    
        Validation done using   
        -> Starting place: attraction with latest opening hours
        -> Final place: attraction with earliest closing time 

'''

#def validateRoute(listofAttra):
apiKey = 'AIzaSyB2NHLaqVDF0uSmuNBMXI3DVsUanzdRD7Q'
url = 'https://maps.googleapis.com/maps/api/directions/json'


class Attraction:
    Category = ""
    Name = ""
    OpeningHours = 0
    ClosingHours = 0
    Latitude = 0
    Longitude = 0
    LatLng = 0
    Duration = 0

    def __init__(self, Category, Name, OpeningHours, ClosingHours, Latitude, Longitude, LatLng, Duration):
        self.Category = Category
        self.Name = Name
        self.OpeningHours = OpeningHours
        self.ClosingHours = ClosingHours
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.LatLng = LatLng
        self.Duration = Duration

totalCostTime = 0;


def getRecommendedTimeSpent(object):
    return int(object['Duration'])


def getTotalCostTime(data, attractions):
    routes = data['routes']
    totalTravelTime = 0
    totalAttractionTime = 0
    for route in routes:
        legs = route['legs']
        for i in range(0, len(legs)):
            currentLeg = legs[i]
            currentTravelTime = round(int(currentLeg['duration']['value']) / 60, 2)
            totalTravelTime += round(currentTravelTime, 2)

            currentAttraction = attractions[i]
            currentAttractionTime = int(currentAttraction.Duration)
            totalAttractionTime += currentAttractionTime

            #print(totalTravelTime)
            #print(totalAttractionTime)

    # nextAttraction = attractions[len(attractions) - 1]
    # nextAttractionTime = int(nextAttraction['Duration'])
    # totalAttractionTime += nextAttractionTime

    #print(totalTravelTime)
    #print(totalAttractionTime)
    return (totalTravelTime + totalAttractionTime)


attractions = []
with open('objects.csv', 'r') as objectsCsv:
    reader = csv.reader(objectsCsv, delimiter=',')
    for row in reader:
        #row = row[0].split('\t')

        #def __init__(self, Category, Name, OpeningHours, ClosingHours, Latitude, Longitude, LatLng, Duration):

        a = Attraction(row[1], row[2], row[3], row[4], row[5], row[6], row[5] + "," + row[6], row[7])
        attractions.append(a)

i = 0
while (1):

    if (i < len(attractions) - 2):
        params = {
            'origin': attractions[i].LatLng,
            'destination': attractions[i + 1].LatLng,
            'key': apiKey,
            'waypoints': attractions[i + 2].LatLng,
            'optimizeWaypoints': 'true'
        }
        r = requests.get(url, params=params)
        data = json.loads(r.text)
        print(data)
        totalCostTime += getTotalCostTime(data, attractions)
        i = i +2
        continue
    if( i + 2 == len(attractions) - 2):
        params = {
            'origin': attractions[i]['LatLng'],
            'destination': attractions[i + 1]['LatLng'],
            'key': apiKey,
        }
        r = requests.get(url, params=params)
        data = json.loads(r.text)
        print(data)
        totalCostTime += getTotalDurationDistance(data, attractions)
    break


print(totalCostTime)

def getLatestOpeningHour(attractions):
    max = 800
    for attr in attractions:
        openingHour = int(attr.OpeningHours)
        if (max < openingHour):
            max = openingHour
    return max


def getEarliestClosingHour(attractions):
    min = 2359
    for attr in attractions:
        closingHour = int(attr.ClosingHours)
        if (min > closingHour):
            min = closingHour
    return min

print(getLatestOpeningHour(attractions))
print(getEarliestClosingHour(attractions))

def validation(totalCostTime, attractions):
    hour = round(totalCostTime/60)
    min = round((totalCostTime%60))*0.6
    tmp = hour*100 + min
    if (getLatestOpeningHour(attractions) + tmp <= getEarliestClosingHour(attractions)):
        return "The Trip is Valid"
    else:
        return "Not enough time to finish the trip"

print(validation(totalCostTime, attractions))