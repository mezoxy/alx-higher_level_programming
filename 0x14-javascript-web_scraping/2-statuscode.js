#!/usr/bin/node
// script that reads and prints the content of a file
const request = require('request');
request(process.argv[2], function (error, response, body) {
  console.log('code:', response.statusCode);
});
