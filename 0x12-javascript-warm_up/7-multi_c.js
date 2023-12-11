#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else if (parseInt(process.argv[2]) <= 0) {
  console.log();
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
	  console.log('C is fun');
  }
}
