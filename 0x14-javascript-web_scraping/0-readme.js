#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');
try {
  const cont = fs.readFileSync(process.argv[2], 'utf8');
  console.log(cont);
} catch (error) {
  console.log('{', error.name + ':', error.message + '\n',
    ' errno:', error.errno + ',\n', ' code:', `'${error.code}'` + ',\n',
    ' syscall:', `'${error.syscall}'` + ',\n', ' path:', `'${error.path}'`, '}');
}
