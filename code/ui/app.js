// Initialize leaflet.js
var L = require('leaflet');
var polyUtil = require('polyline-encoded')

// Initialize the map
var map = L.map('map', {
  scrollWheelZoom: true
});

var backendUrl = "http://localhost:5000/suggest"
//var backendUrl = "http://localhost:3000/suggest"


// Set the position and zoom level of the map
map.setView([53.353645, -6.371059], 13);


// Create control that shows information on hover
var info = L.control({position:'topright'});

/* Base Layers */
var esri_WorldImagery = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attributions: 'www.tphangout.com',
  maxZoom: 18
}).addTo(map);

var latestData;
var currentRoute = 0

document.getElementById ("startBtn").addEventListener ("click", function(){

  currentRoute = 0;
  getNextRoute()
});


document.getElementById ("newUser").addEventListener ("click", function(){
  console.log("~~~")
  window.location.href = "/Registry"
});

document.getElementById ("existingUser").addEventListener ("click", function(){
  console.log("~~~")
  //test()
  window.location.href = "/Login"
});


document.getElementById ("Mary").addEventListener ("click", function(){
  var returnJson = new Object();
  returnJson.user_id = '';//need to fill in
  returnJson.name = 'Mary';
  returnJson.tags = ['food','pubs','nature'];
  returnJson.age = 23;
  returnJson.gender = 'F';
  returnJson.avgDuration = 6;
  returnJson.avgBudget = '1';
  returnJson = JSON.stringify(returnJson);
  currentRoute = 0;
  console.log(returnJson);
  var axiosConfig = {
    headers: {
      'Content-Type': 'application/json',
      'accept': '*/*',
    }
  };
  const ax = require('axios');

  ax.post(backendUrl, returnJson, axiosConfig).then(resp => {
  //ax.get(backendUrl, axiosConfig).then(resp => {
    console.log(resp.data['places']);
    latestData = resp.data['places']

    var Start = new Object()
    var geoLoc = new Object()
    geoLoc.latitude = 53.338764
    geoLoc.longitude = -6.256116
    Start.geoLocation = geoLoc

    var hours = new Object()
    hours.closing = 2359
    hours.opening = 800
    Start.hours = hours

    var bestTimeToVisit = new Object()
    bestTimeToVisit.day = "N/A"
    bestTimeToVisit.season = "N/A"
    Start.bestTimeToVisit = bestTimeToVisit

    Start.name = "Your hotel - The Shelbourne"
    Start.review = 5.0
    duration = 0

    latestData.unshift(Start)
    getNextRoute()
  }).catch(error => {
    console.log(error);
  });
});




document.getElementById ("nextBtn").addEventListener ("click", getNextRoute);


function getNextRoute(){
  var lat = latestData[currentRoute]['geoLocation']['latitude']
  var lng = latestData[currentRoute]['geoLocation']['longitude']

  start = lat+","+lng
  dest = latestData[currentRoute+1]['geoLocation']['latitude']+","+latestData[currentRoute+1]['geoLocation']['longitude']


  console.log(latestData[currentRoute])
  getRoute(start, dest)
  currentRoute +=1
}


  //ToDo change method to take in starting lat/long and route to destination lat/long
  function getRoute(start, destination){
    if(start == ""){
      alert("Starting location cannot be empty!")
      return;
    }

    if(destination == ""){
      alert("Destination location cannot be empty!")
      return;
    }
    console.log("Routing from ::"+start+"  ::  "+destination)

    var url = "https://maps.googleapis.com/maps/api/directions/json?&origin="+start+"&destination="+destination+"&key=AIzaSyB2NHLaqVDF0uSmuNBMXI3DVsUanzdRD7Q"
    console.log(url)
    const http = require('http')
    http.get(url, (resp) => {
      let data = '';
      // A chunk of data has been recieved.
      resp.on('data', (chunk) => {
        data += chunk;
      });

      // The whole response has been received. Print out the result.
      resp.on('end', () => {
        drawPolyline(JSON.parse(data))
      });

    }).on("error", (err) => {
      console.log("Error: " + err.message);
      console.log("Retrying...")
      getRoute(start, destination)
    });
  }

var startMarker;
var destMarker;
var prevPolyline = []

function drawPolyline(jsonData){
    if (startMarker) {
      map.removeLayer(startMarker);
    }
    if (destMarker) {
      map.removeLayer(destMarker);
    }
    //console.log(prevPolyline)
    if (prevPolyline) {
      for(stepPolyline in prevPolyline){
        map.removeLayer(prevPolyline[stepPolyline]);
      }
      prevPolyline = []
    }

    let markerGroup = L.featureGroup()

      jsonData = jsonData['routes']

      jsonData.forEach(function(route) {
            var legs = route['legs']

            legs.forEach(function(leg){
              var steps = leg['steps']
              var color = "#"+((1<<24)*Math.random()|0).toString(16)

              var startMarkerLatLng = [steps[0]['start_location']["lat"], steps[0]['start_location']["lng"]]
              var destMarkerLatLng = [steps[steps.length-1]['end_location']['lat'],steps[steps.length-1]['end_location']['lng']]


              startMarker = L.marker([startMarkerLatLng[0], startMarkerLatLng[1]]).addTo(map).on('click', function(e){
                alert("Clicked start..")
                console.log(latestData)
              });
              destMarker = L.marker([destMarkerLatLng[0], destMarkerLatLng[1]]).addTo(map).on('click', function(e){
                var current = latestData[currentRoute]
                console.log(current)
                alert(current.name+"\n\n"
                      +"Category: "+current.category+"\n"
                      +"Duration: "+current.duration+" minutes \n"
                      +"Review: "+current.review+"/5")
              });
              steps.forEach(function(step){
                var polyline = step['polyline']['points']
                var coordinates = polyUtil.decode(polyline);

                var polyline = L.polyline(coordinates, {
                  color: color,
                  weight: 10,
                  opacity: .7,
                  dashArray: '0,0',
                  lineJoin: 'round'
                }).addTo(map)

                if(prevPolyline){
                  prevPolyline.push(polyline)
                }
              })
            })
      })
  }
/*
function test(){
    var url = "http://localhost:5000/1"
  const http = require('http')
      http.get(url, (resp) => {
        let data = '';

        // A chunk of data has been recieved.
        resp.on('data', (chunk) => {
          data += chunk;
        });

        // The whole response has been received. Print out the result.
        resp.on('end', () => {
          latestData = JSON.parse(data)['places']

          getNextRoute()

        });

      }).on("error", (err) => {
        console.log("Error: " + err.message);
      });
}*/


  function handleResponse(data){

    var username = data['user_name']
    var places = data['places']
    var currentPlaceLatLng;
    var previousPlaceLatLng = "Dublin";
    i=0
    for(i =0; i < places.length -1; i++){
      var geoLoc = places[i]['geoLocation']

      var currentPlaceLatLng = parseFloat(geoLoc['latitude'])+","+parseFloat(geoLoc['longitude'])
      getRoute(previousPlaceLatLng, currentPlaceLatLng )
      previousPlaceLatLng = currentPlaceLatLng
    }
  }
