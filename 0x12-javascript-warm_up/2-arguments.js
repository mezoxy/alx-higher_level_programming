#!/usr/bin/node
const Args = process.argv;

if (Args.length > 2) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
