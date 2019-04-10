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
var requestData = ""


document.getElementById ("startBtn").addEventListener ("click", function(){
  requestData = window.localStorage.getItem("data")
  localStorage.removeItem("data");
  currentRoute = 0;

  const ax = require('axios');
  var axiosConfig = {
    headers: {
      'Content-Type': 'application/json',
      'accept': '*/*',
    }
  };
  console.log("Sending post.........")
  ax.post('http://localhost:5000/suggest', requestData, axiosConfig).then(resp => {
    console.log(resp)
    resp = resp.data
    console.log(resp)
    returnUserId = resp.user_id;
    alert(returnUserId);
    latestData = resp.places;

    var Start = new Object()
    var geoLoc = new Object()
    geoLoc.latitude = 53.428049
    geoLoc.longitude = -6.224406
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
      //'accept': '*/*',
      //'Access-Control-Allow-Origin': '*',
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
  start = latestData[currentRoute]['geoLocation']['latitude']+","+latestData[currentRoute]['geoLocation']['longitude']
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










/****************form*******************/

var returnUserId;

function getUserId() {
  var userid = document.getElementById("UserId").value;
  return userid;
}

function getUsername() {
  var username = document.getElementById("Username").value;
  return username;
}

function getDuration() {
  var duration = document.getElementById("Duration").value;
  alert(duration);
  return duration;
}

function getAge() {
  var age = document.getElementById("Age").value;
  return age;
}

function getGender() {
  //alert("setting age");
  var gender = document.getElementById("Gender").value;
  //alert(e);
  //var gender = e.options[e.selectedIndex].value;
  alert(gender);
  return gender;
}

function getBudget() {
  var tmp = document.getElementById("Budget").value;
  //var tmp = e.options[e.selectedIndex].value;
  var budget = 99;
  switch (tmp) {
    case '$':
      budget = 0;
      break;
    case '$$':
      budget = 1;
      break;
    case '$$$':
      budget = 2;
      break;
    default:
      break;
  }
  return budget;
}

function getPre() {
  var preference = ['', '', ''];
  var inputTag = ['','',''];
  var tags = document.getElementById("tags");
  var i = 0;
  for (var j = 0; j < 12; j ++){
    if(tags.options[j].selected){
      inputTag[i]=tags.options[j].value;
      alert(inputTag[i]);
      i ++;
    }
  }
  for (i = 0; i < 3; i++) {
    switch (inputTag[i]) {
      case ('1'):
        preference[i] = "outdoor";
        break;
      case ('2'):
        preference[i] = "museum";
        break;
      case ('3'):
        preference[i] = "historic";
        break;
      case ('4'):
        preference[i] = "park";
        break;
      case ('5'):
        preference[i] = "lake";
        break;
      case ('6'):
        preference[i] = "food";
        break;
      case ('7'):
        preference[i] = "pubs";
        break;
      case ('8'):
        preference[i] = "play";
        break;
      case ('9'):
        preference[i] = "movie";
        break;
      case ('10'):
        preference[i] = "styling";
        break;
      case ('11'):
        preference[i] = "attire";
        break;
      case ('12'):
        preference[i] = "shoes";
        break;
      default:
        preference[i] = "";
        break;

    }
    alert(preference[i])
  }
  return preference;
}

function setPrefNew() {
  alert("in setpref new....")
  var returnJson = new Object();
  returnJson.user_id = '';
  returnJson.name = getUsername();
  returnJson.age = getAge();
  returnJson.gender = getGender();
  returnJson.avgDuration = getDuration();
  returnJson.avgBudget = getBudget();
  returnJson.tags = getPre();

  returnJson = JSON.stringify(returnJson);

  setPrefNewResult = returnJson
  console.log("returning: "+returnJson);
  window.localStorage.setItem("data", returnJson)
}

function setPrefOld() {
  var returnJson = new Object();
  returnJson.user_id = getUserId();
  returnJson.name = '';
  returnJson.tags = getPre();
  returnJson.age = 0;
  returnJson.gender = '';
  returnJson.avgDuration = getDuration();
  returnJson.avgBudget = getBudget();
  returnJson = JSON.stringify(returnJson);
  console.log(returnJson);

  setPrefNewResult = returnJson
  console.log("returning: "+returnJson);
  window.localStorage.setItem("data", returnJson)

}
