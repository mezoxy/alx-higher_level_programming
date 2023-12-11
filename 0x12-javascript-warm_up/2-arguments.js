#!/usr/bin/node
const Args = process.argv;

if (Args.length <= 2) {
  console.log('No argument');
} else if (Args.length == 3) {
  console.log('Argument found');
} else {
	console.log('Arguments found');
}
