#!/usr/bin/node
// script that reads and prints the content of a file
const request = require('request');
request(process.argv[2], function (error, response, body) {
	if (err) {
		console.log("error");
	} else {
		let num = 0;
		const lis = JSON.parse(body).results;
		for (let item in lis) {
			if (item.hasOwnPropert("characters")) {
				for (let ur in item["characters"]) {
					if (ur == "https://swapi-api.alx-tools.com/api/people/18/") {
						num++;
					}
				}
			}
		}
		console.log(num);
	}
});
