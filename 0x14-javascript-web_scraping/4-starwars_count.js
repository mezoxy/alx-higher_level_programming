#!/usr/bin/node
// script that reads and prints the content of a file
const request = require('request');
const ID = '18'
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('Error accured');
  } else {
    const data = JSON.parse(body);
    const ur = data.characters[17];
    request(ur, function (error, response, body) {
      if (error) {
	console.log('Error accured');
      } else {
	      const data = JSON.parse(body);
	      const nmb = data.films.lenght;
	      console.log(nmb);
      }
  });
});
