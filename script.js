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
