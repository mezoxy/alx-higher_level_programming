#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < parseInt(process.argv[2])) {
    console.log('X'.repeat(parseInt(process.argv[2])));
    i++;
  }
}
