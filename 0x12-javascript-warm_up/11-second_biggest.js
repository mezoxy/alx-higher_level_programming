#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 0; i < process.argv.length - 2; i++) {
    arr[i] = parseInt(process.argv[i + 2]);
  }
  arr.sort();
  console.log(arr[arr.length - 2]);
}
