#!/usr/bin/node
// script that reads and prints the content of a file
const request = require('request');
const ID = '18'
request(process.argv[2], function (error, response, body) {
	if (err) {
		console.log("error");
	} else {
		const charc = JSON.parse(body).characters;
		for (let i = 0; i < charc.lenght; i++) {
			if (charc[i] == "https://swapi-api.alx-tools.com/api/people/18/") {
				const request = require('request');
				request("https://swapi-api.alx-tools.com/api/people/18/"function (error, response, body) {
					if (err) {
						console.log("error");
					} else {
						const nmb = JSON.parse(body).films.lenght;
						console.log(nmb);
						break;
					}
				});
			}
		}
	}
});
