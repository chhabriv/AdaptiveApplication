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

document.getElementById ("startBtn").addEventListener ("click", getLatestData);

function getLatestData(){

  currentRoute = 0

  var url = "http://localhost:3000/getRoutes"
  const http = require('http')
      http.get(url, (resp) => {
        let data = '';

        // A chunk of data has been recieved.
        resp.on('data', (chunk) => {
          data += chunk;
        });

        // The whole response has been received. Print out the result.
        resp.on('end', () => {
          latestData = JSON.parse(data)


          getRoute(latestData[currentRoute].Origin, latestData[currentRoute].Destination)
          currentRoute +=1
        });

      }).on("error", (err) => {
        console.log("Error: " + err.message);
      });
}

document.getElementById ("newUser").addEventListener ("click", function(){
  console.log("~~~")
  window.location.href = "/Registry"
});

document.getElementById ("existingUser").addEventListener ("click", function(){
  console.log("~~~")
  window.location.href = "/Login"
});

document.getElementById ("login").addEventListener ("click", setPrefExisting);
document.getElementById ("signup").addEventListener ("click", setPrefNew);

document.getElementById ("nextBtn").addEventListener ("click", getNextRoute);
function getNextRoute(){

  getRoute(latestData[currentRoute].Origin, latestData[currentRoute].Destination)
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
    console.log(prevPolyline)
    if (prevPolyline) {
      for(stepPolyline in prevPolyline){
        console.log("removing"+stepPolyline)
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

                prevPolyline.push(polyline)
              })
            })
      })
  }

  function getUsername() {
    var username = document.getElementById("Username").value;
    return username;
  }

  function getUserId() {
    var userid = document.getElementById("UserId").value;
    return userid;
  }

  function getGender() {
    var gender = document.getElementById("Gender").value;
    return gender;
  }
  function getAge() {
    var age = document.getElementById("Age").value;
    return age;
  }

  function getDuration() {
    var duration = document.getElementById("Duration").value;
    return duration;
  }

  function getBudget(){
    var tmp = document.getElementById("Budget").value;
    var budget = 9;
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
    var preference=['','',''];
    var inputTag = [document.getElementById("tag1").value,document.getElementById("tag2").value,document.getElementById("tag3").value];
    var i = 0;
    for (i = 0; i < 3; i++) {
      switch (inputTag[i]) {
        case 1:
          preference[i] = "outdoor";
          break;
        case 2:
          preference[i] = "museum";
          break;
        case 3:
          preference[i] = "historic";
          break;
        case 4:
          preference[i] = "park";
          break;
        case 5:
          preference[i] = "lake";
          break;
        case 6:
          preference[i] = "food";
          break;
        case 7:
          preference[i] = "pubs";
          break;
        case 8:
          preference[i] = "play";
          break;
        case 9:
          preference[i] = "movie";
          break;
        case 10:
          preference[i] = "styling";
          break;
        case 11:
          preference[i] = "sttire";
          break;
        case 12:
          preference[i] = "shoes";
          break;
        default:
          break;
      }
    }
    return preference;
  }
  function submit_user() {
    var username = document.getElementById("Name").value;
    var age = document.getElementById("Age").value;
    var duration = document.getElementById("Duration").value;
    var gender = document.getElementById("Gender").value;
    var budget = document.getElementById("Budget").value
    var inputTag1 = document.getElementById("tag1").value;
    var inputTag2 = document.getElementById("tag2").value;
    var inputTag3 = document.getElementById("tag3").value;
    alert(username);
}
  function setPrefExisting() {
    console.log('ExistingUser');
    var userid = getUserId();
    var preference = getPre();
    var duration = getDuration();
    var budget = getBudget();
    let returnJson = '{\"userid\":'+ userid+',\"username\":\"null\",\"age\":0,\"gender\":\"null\",\"duration\":'+duration+',\"budget\":'+budegt +',\"tag\":['+preference[0]+','+preference[1]+','+preference[2]+']}';
    console.log(returnJson);
    var axiosConfig = {
        headers: {
            'Content-Type': 'application/json',
            'accept' : '*/*',
        }
      };
      ax.post('url to service', returnJson, axiosConfig).then(resp => {
        console.log(resp);
      }).catch(error => {
      console.log(error);
      });
    }

    function setPrefNew() {
      console.log('New User');
      var username = getUsername();
      var age = getAge();
      var gender = getGender();
      var preference = getPre();
      var duration = getDuration();
      var budget = getBudget();
      let returnJson = '{\"userid\":\"null\"'+',\"username\":'+ username+',\"age\":'+age+',\"gender\":'+gender+',\"duration\":'+duration+',\"budget\":'+budegt + ',\"tag\":['+preference[0]+','+preference[1]+','+preference[2]+']}';
      console.log(returnJson);
      var axiosConfig = {
          headers: {
              'Content-Type': 'application/json',
              'accept' : '*/*',
          }
        };
        ax.post('http://localhost:500/suggest', returnJson, axiosConfig).then(resp => {
          console.log(resp);
        }).catch(error => {
        console.log(error);
        });
      }
