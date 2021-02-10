let pclass = document.querySelector(".p-class");   
  let button1 = document.querySelector(".button1")
   

   
   
   // Your web app's Firebase configuration
   var firebaseConfig = {
    apiKey: "AIzaSyDiEMKFF3n5hSDBb6xLsXoHclz_6bK_9wk",
    authDomain: "aslproject-7fabb.firebaseapp.com",
    databaseURL: "https://aslproject-7fabb.firebaseio.com",
    projectId: "aslproject-7fabb",
    storageBucket: "aslproject-7fabb.appspot.com",
    messagingSenderId: "4437569972",
    appId: "1:4437569972:web:70d9da46cbd6d2f97e42e1"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  let database = firebase.database().ref();
  console.log(database);

  database.on('child_added', (data) => {
let h = document.createElement("p");


console.log(data.val().Character);
 h.innerHTML  = data.val().Character;
  document.body.appendChild(h);



});
var video = document.getElementById('video');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    });
}

// button1.addEventListener("click",() => {
//   database.remove();
//  stop();
   

// });

// var video = document.querySelector("#videoElement");

// if (navigator.mediaDevices.getUserMedia) {
//   navigator.mediaDevices.getUserMedia({ video: true })
//     .then(function (stream) {
//       video.srcObject = stream;
//     })
//     .catch(function (err0r) {
//       console.log("Something went wrong!");
//     });
// }

// function stop() {
//   var stream = video.srcObject;
//   var tracks = stream.getTracks();

//   for (var i = 0; i < tracks.length; i++) {
//     var track = tracks[i];
//     track.stop();
//   }

//   video.srcObject = null;
// }