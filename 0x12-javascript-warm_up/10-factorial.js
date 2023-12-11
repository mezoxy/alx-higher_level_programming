#!/usr/bin/node
function fact (a) {
  if (a === 0 || isNaN(a)) {
    return (1);
  } else {
    return (a * fact(a - 1));
  }
}

const a = parseInt(process.argv[2]);
console.log(fact(a));
