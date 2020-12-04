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

button1.addEventListener("click",() => {
  database.remove();
 
    location.reload();

});

