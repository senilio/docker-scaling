var express = require('express');
var app = express();

app.get('/', function (req, res) {
  res.send(process.env.HOSTNAME);
});

var server = app.listen(3000, function () {
  console.log('Server started');
});
