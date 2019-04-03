function showname() {
  var username = document.getElementById("username").value;
  var inputTag1 = document.getElementById("tag1").value;
  var inputTag2 = document.getElementById("tag2").value;
  var inputTag3 = document.getElementById("tag3").value;

  alert(username + inputTag1 + inputTag2 + inputTag3);
}

function getUsername() {
  var username = document.getElementById("username").value;

  return username;
}

function getPre() {
  var prefernce[3];
  var inputTag[3];
  inputTag[0] = document.getElementById("tag1").value;
  inputTag[1] = document.getElementById("tag2").value;
  inputTag[2] = document.getElementById("tag3").value;
  for (var i = 0; i < 3; i++) {
    switch (inputTag[i]) {
      case 1:
        preference[i] = "";
        break;
      case 2:
        preference[i] = "";
        break;
      case 3:
        preference[i] = "";
        break;
      case 4:
        preference[i] = "";
        break;
      case 5:
        preference[i] = "";
        break;
      case 6:
        preference[i] = "";
        break;
      case 7:
        preference[i] = "";
        break;
      case 8:
        preference[i] = "";
        break;
      case 9:
        preference[i] = "";
        break;
      case 10:
        preference[i] = "";
        break;
      case 11:
        preference[i] = "";
        break;
      case 12:
        preference[i] = "";
        break;
      case 13:
        preference[i] = "";
        break;
      case 14:
        preference[i] = "";
        break;
      case 15:
        preference[i] = "";
        break;
      default:
        preference[i] = "";
        break;

    }
  }
  return preference
}

function setPref() {
  var username = getUsername();
  var preference[] = getPre();
  var returnJson = "\"username\":"+username+"\"tag1\":"+preference[0]+"\"tag1\":"+preference[1]+"\"tag1\":"+preference[2];
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
