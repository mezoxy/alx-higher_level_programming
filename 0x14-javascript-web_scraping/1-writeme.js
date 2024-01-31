#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');
try {
  fs.writeFileSync(process.argv[2], process.argv[3], 'utf8');
} catch (error) {
  console.log('{', error.name + ':', error.message + '\n',
    ' errno:', error.errno + ',\n', ' code:', `'${error.code}'` + ',\n',
    ' syscall:', `'${error.syscall}'` + ',\n', ' path:', `'${error.path}'`, '}');
}
