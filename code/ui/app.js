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

var startMarker;
var destMarker;
var prevPolyline = []
document.getElementById ("startBtn").addEventListener ("click", test);


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
  console.log(returnJson);
  alert(returnJson);
  alert('hdgy');
  var axiosConfig = {
    headers: {
      'Content-Type': 'application/json',
      //'accept': '*/*',
      //'Access-Control-Allow-Origin': '*',
    }
  };
  const ax = require('axios');

  ax.post('http://127.0.0.1:5000/suggest', returnJson, axiosConfig).then(resp => {
    console.log(resp.data['places']);
    latestData = resp.data['places']
    getNextRoute()
  }).catch(error => {
    console.log(error);
  });
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
    return duration;
  }

  function getAge() {
    var age = document.getElementById("Age").value;
    return age;
  }

  function getGender() {
    var gender = document.getElementById("Gender").value;
    return gender;
  }

  function getBudget() {
    var tmp = document.getElementById("Budget").value;
    alert(tmp)
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
    alert(budget);
    return budget;
  }

  function getPre() {
    var preference = ['', '', ''];
    var inputTag = [document.getElementById("tag1").value, document.getElementById("tag2").value, document.getElementById("tag3").value];

    for (var i = 0; i < 3; i++) {
      switch (inputTag[i]) {
        case ('1'):
          //alert(preference[i])
          preference[i] = "outdoor";
          //alert(preference[i])
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
          preference[i] = "sttire";
          break;
        case ('12'):
          preference[i] = "shoes";
          break;
        default:
          //preference[i] = "";
          break;

      }
      //alert(preference[i])
    }
    return preference;
  }

  function setPrefNew() {
    var returnJson = new Object();
    returnJson.user_id = '';
    returnJson.name = getUsername();
    returnJson.tags = getPre();
    returnJson.age = getAge();
    returnJson.gender = getGender();
    returnJson.avgDuration = getDuration();
    returnJson.avgBudget = getBudget();
    returnJson = JSON.stringify(returnJson);
    console.log(returnJson);
    var axiosConfig = {
      headers: {
        'Content-Type': 'application/json',
        'accept': '*/*',
      }
    };
    alert('11');
    const ax = require('axios');
    ax.post('http://localhost:5000/suggest', returnJson, axiosConfig).then(resp => {
      console.log(resp.data['places']);
      alert(resp.data['user_id'])
      latestData = resp.data['places'];
      //getNextRoute()
      alert(latestData);
    }).catch(error => {
      console.log(error);
    });

  }

  function setPrefOld() {
    var returnJson = new Object();
    returnJson.user_id = getUserId();
    returnJson.name = '';
    returnJson.tags = getPre();
    returnJson.age = '';
    returnJson.gender = '';
    returnJson.avgDuration = getDuration();
    returnJson.avgBudget = getBudget();
    returnJson = JSON.stringify(returnJson);
    console.log(returnJson);
    //alert('hdgy');
    // var axiosConfig = {
    //   headers: {
    //     'Content-Type': 'application/json',
    //     'accept': '*/*',
    //   }
    // };
    // ax.post('url to service', returnJson, axiosConfig).then(resp => {
    //   console.log(resp);
    // }).catch(error => {
    //   console.log(error);
    // });

  }









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
