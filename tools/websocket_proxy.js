/*
TODO: the proxy doesn't work properly, probably due to race conditions
...but at least, it doesn't crash like with FastAPI/sanic/websockets.

Looking for a python solution, but any other language is fine too.
*/

var express = require('express');
var app = express();
var expressWs = require('express-ws')(app);
var net = require('net');

// remember to replace the Telegram Web websocket url
// with `ws://127.0.0.1/proxy`
app.ws('/proxy', function (ws, req) {
    console.info("new connection detected");
    let conn = new net.Socket();
    conn.connect(4430, '127.0.0.1', () => {
        ws.on('message', function (msg) {
            conn.write(msg);
        }).on('close', function () {
            conn.end();
        });
    }).on('data', (data) => {
        ws.send(data);
    }).on('close', () => {
        ws.close();
    });
});

// remember to replace the port too
console.log("Running on port 3000...")
app.listen(3000);
