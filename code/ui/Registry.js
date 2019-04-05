function getUsername() {
  var username = document.getElementById("Username").value;
  alert(username);
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
  var gender = document.getElementById("Gender").value;
  alert(gender);
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
    alert(preference[i])
  }
  return preference;
}

function setPref() {
  var returnJson = new Object();
  returnJson.userid = '';
  returnJson.name = getUsername();
  returnJson.preference = getPre();
  returnJson.age = getAge();
  returnJson.gender = getGender();
  returnJson.duration = getDuration();
  returnJson.budget = getBudget();
  //var returnJson = '{"username":"' + username + '","age":' + age + ',"gender":"' + gender + '","duration":"' + duration + '","budget":"' + budegt + '","tag1":[' + preference[0] + ',' + preference[1] + ',' + preference[2] + ']}';
  returnJson = JSON.stringify(returnJson);
  console.log(returnJson);
  alert("11");
  window.location.href="http://127.0.0.1:9966";
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
