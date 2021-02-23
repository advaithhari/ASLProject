const multer = require('multer');
const express = require('express')

const {PythonShell} =require('python-shell'); 
const {
    spawn
} = require('child_process');
const http = require('http');
const app = express()
const port = 5621
var useMulter = multer();
app.post('/uploadUserBook',useMulter.any(),(req,res)=>{
    console.log("reached upload user book post request")
    if(req.files.length>0){
        console.log(req.files[0].buffer.length);
        console.log(req.files[0]);
        var dataToSend;
        // spawn new child process to call the python script
        const python = spawn('python', ['testSignLangNN.py']);
        // collect data from script
        python.stdout.on('data', function (data) {
            console.log('Pipe data from python script ...');
            dataToSend = data.toString();
        });
        //in close event we are sure that stream from child process is closed
        python.on('close', (code) => {
            console.log(`child process close all stdio with code ${code}`);
            // send data to browser
            //location.href = "localhost:3000?id="+dataToSend;

            console.log(dataToSend)
            res.send(dataToSend)

        });
    }
});
app.get('/python', (req, res) => {

    

})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))