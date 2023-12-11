#!/usr/bin/node

function add (a, b){
  if (a == null || b == null) {
    return ('NaN');
  } else {
    return (a + b);
  }
}

const c = parseInt(process.argv[2]);
const d = parseInt(process.argv[3]);
console.log(add(c, d));
