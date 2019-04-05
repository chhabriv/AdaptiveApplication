


function getUserId() {
  var userid = document.getElementById("UserId").value;
  return userid;
}

function getDuration() {
  var duration = document.getElementById("Duration").value;
  return duration;
}

function getBudget() {
  var tmp = document.getElementById("Budget").value;
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
        preference[i] = "";
        break;
    }
    alert(preference[i])
  }
  return preference;
}

function setPref() {
  var returnJson = new Object();
  returnJson.userid = getUserId();
  alert("setting name");
  returnJson.name = "";
  alert("setting pref");
  returnJson.preference = getPre();
  alert("setting age");
  returnJson.age = 0;
  returnJson.gender = "";
  returnJson.duration = getDuration();
  returnJson.budget = getBudget();
  //let returnJson = '{\"userid\":' + userid + '\"duration\":' + duration + '\"budget\":' + budegt + '\"tag\":['+preference[0]+','+preference[1]+','+preference[2]+']}';
  returnJson = JSON.stringify(returnJson);
  alert(returnJson);
  var axiosConfig = {
    headers: {
      'Content-Type': 'application/json',
      'accept': '*/*',
    }
  };
  ax.post('url to service', returnJson, axiosConfig).then(resp => {
    console.log(resp);
  }).catch(error => {
    console.log(error);
  });
}
