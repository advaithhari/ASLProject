let pclass = document.querySelector(".p-class");   
  let button1 = document.querySelector(".button1")
   

   
   
  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyBli-KhJRDRa-fnWyeSIELr1mMZ4K6n2RE",
    authDomain: "projectasl.firebaseapp.com",
    projectId: "projectasl",
    storageBucket: "projectasl.appspot.com",
    messagingSenderId: "942372278020",
    appId: "1:942372278020:web:038cb7d411e2dbcb45ca51",
    measurementId: "G-9942EW0HYY"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();

button1.addEventListener("click",() => {
  database.remove();
 stop();
   

});

var video = document.querySelector("#videoElement");

if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
    })
    .catch(function (err0r) {
      console.log("Something went wrong!");
    });
}
let frames ;
function stop() {
  var stream = video.srcObject;
  var tracks = stream.getTracks();
  frames = stream;
  for (var i = 0; i < tracks.length; i++) {
    var track = tracks[i];
    track.stop();
  }

  video.srcObject = null;
}


let database = firebase.database().ref();
console.log(database);

database.on('child_added', (data) => {
let h = document.createElement("p");


console.log(data.val().Character);
h.innerHTML  = data.val().Character;
document.body.appendChild(h);

value = {
  frame: frame

}
console.log
database.push(value);

});
