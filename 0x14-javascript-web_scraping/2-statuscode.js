#!/usr/bin/node
// script that reads and prints the content of a file
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('Error accured');
  } else {
    console.log('code:', response.statusCode);
  }
});
