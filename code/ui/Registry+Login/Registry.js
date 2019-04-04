


function showinfo() {
  var username = document.getElementById("Name").value;
  var age = document.getElementById("Age").value;
  var duration = document.getElementById("Duration").value;
  var gender = document.getElementById("Gender").value;
  var budget = document.getElementById("Budget").value
  var inputTag1 = document.getElementById("tag1").value;
  var inputTag2 = document.getElementById("tag2").value;
  var inputTag3 = document.getElementById("tag3").value;

  alert(username + inputTag1 + inputTag2 + inputTag3);
}

function getAge() {
  var username = document.getElementById("Age").value;

  return username;
}
function getUsername() {
  var username = document.getElementById("Name").value;

  return username;
}
function getDuration() {
  var username = document.getElementById("Duration").value;

  return username;
}
function getGender() {
  var username = document.getElementById("Gender").value;

  return username;
}
function getBudget(){
  var tmp = document.getElementById("Budget").value;
  var budget = 0;
  switch (budget) {
    case '$':
       budget = 0;
      break;
    case '$$':
      budget = 1;
      break;
    case '$$$':
      budget = 2;
      break;
}

function getPre() {
  var prefernce=['','',''];
  var inputTag = [document.getElementById("tag1").value,document.getElementById("tag2").value,document.getElementById("tag3").value];
  for (var i = 0; i < 3; i++) {
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
        preference[i] = "";
        break;

    }
  }
  return preference;
}
document.getElementById ("submit").addEventListener ("click", setPref);

function setPref() {
  console.log('hdgy');
  var username = getUsername();
  var preference = getPre();
  var age = getAge();
  var gender = getGender();
  var duration = getDuration();
  var budget = getBudget();
  let returnJson = '{\"username\":'+ username+'\"age\":'+age+'\"gender\":'+gender+'\"duration\":'+duration+'\"budget\":'+budegt + '\"tag1\":'+preference[0]+'\"tag2\":'+preference[1]+'\"tag3\":'+preference[2]+'}';
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

}
