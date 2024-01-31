#!/usr/bin/node
// script that reads and prints the content of a file
const request = require('request');
const ur = 'https://swapi-api.alx-tools.com/api/films/'
request(ur + process.argv[2], function (error, response, body) {
  if (error) {
    console.log('Error accured');
  } else {
    const data = JSON.parse(body);
    
    console.log(data.title);
  }
});
