#!/usr/bin/node
const req = require('request');

req(process.argv[2], function (err, response, body) {
  if (err) {
    console.log('Error');
  } else {
    const fs = require('fs');
    try {
      fs.writeFileSync(process.argv[3], body, 'utf8');
    } catch (err) {
      console.log("File doesn't exist");
    }
  }
});
