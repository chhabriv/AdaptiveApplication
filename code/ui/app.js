// Initialize leaflet.js
var L = require('leaflet');
var polyUtil = require('polyline-encoded')

// Initialize the map
var map = L.map('map', {
  scrollWheelZoom: true
});

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

document.getElementById ("startBtn").addEventListener ("click", test);


document.getElementById ("newUser").addEventListener ("click", function(){
  console.log("~~~")
  window.location.href = "/Registry"
});

document.getElementById ("existingUser").addEventListener ("click", function(){
  console.log("~~~")
  test()
  //window.location.href = "/Login"
});

document.getElementById ("nextBtn").addEventListener ("click", getNextRoute);


function getNextRoute(){

  var lat = latestData[currentRoute]['geoLocation']['latitude']
  var lng = latestData[currentRoute]['geoLocation']['longitude']

  var start;
  var dest;

  if(currentRoute == 0){
    start = "Dublin"
    dest = lat+","+lng
  }
  else{
    start = lat+","+lng
    dest = latestData[currentRoute+1]['geoLocation']['latitude']+","+latestData[currentRoute+1]['geoLocation']['longitude']
  }


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

    var url = "https://maps.googleapis.com/maps/api/directions/json?&origin="+start+"&destination="+destination+"&key=AIzaSyB2NHLaqVDF0uSmuNBMXI3DVsUanzdRD7Q"
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


              startMarker = L.marker([startMarkerLatLng[0], startMarkerLatLng[1]])
              destMarker = L.marker([destMarkerLatLng[0], destMarkerLatLng[1]])
              markerGroup.addLayer(startMarker);
              markerGroup.addLayer(destMarker);
              map.addLayer(markerGroup);

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

function test(){
  var url = "http://localhost:3000/1"
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
}


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
