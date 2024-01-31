#!/usr/bin/node
// script that reads and prints the content of a file
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('error');
  } else {
    let num = 0;
    const lis = JSON.parse(body).results;
    for (const item in lis) {
      if (lis[item].characters) {
        for (const ur in lis[item].characters) {
          if (lis[item].characters[ur] === 'https://swapi-api.alx-tools.com/api/people/18/' || lis[item].characters[ur] === 'http://swapi-api.alx-tools.com/api/people/18/') {
            num++;
          }
        }
      }
    }
    console.log(num);
  }
});
