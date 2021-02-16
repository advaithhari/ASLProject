const express = require('express')
const {spawn} = require('child_process');
const http = require('http');
const app = express()
const port = 3000
app.use('/assets', [
    express.static(__dirname + '/node_modules/jquery/dist/'),
    express.static(__dirname + '/node_modules/materialize-css/dist/'),
    
]);
app.get('/', (req, res) => {
 
 var dataToSend;
 // spawn new child process to call the python script
 const python = spawn('python', ['plottinggraph.py']);
 // collect data from script
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  dataToSend = data.toString();
 });
 // in close event we are sure that stream from child process is closed
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
 //location.href = "localhost:3000?id="+dataToSend;

 console.log(dataToSend)
 res.send(dataToSend)

 });
 
})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))
