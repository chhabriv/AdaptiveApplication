function getUserId() {
  var username = document.getElementById("UserId").value;
  alert(username);
  return username;
}

function getDuration() {
  var username = document.getElementById("Duration").value;
  return username;
}

function getBudget() {
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
    default:
      break;
  }
}

function getPre() {
  var prefernce = ['', '', ''];
  var inputTag = [document.getElementById("tag1").value, document.getElementById("tag2").value, document.getElementById("tag3").value];
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

function setPref() {
  alert('hdgy');
  var userid = getUserId();
  var preference = getPre();
  var duration = getDuration();
  var budget = getBudget();
  let returnJson = '{\"userid\":' + userid + '\"duration\":' + duration + '\"budget\":' + budegt + '\"tag\":['+preference[0]+','+preference[1]+','+preference[2]+']}';
  console.log(returnJson);
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
