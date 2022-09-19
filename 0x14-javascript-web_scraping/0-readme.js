#!/usr/bin/node
const fs = require('fs');
const myArgs = String(process.argv.slice(2));
const filename = myArgs.replace('[ ', '');

try {
  const data = fs.readFileSync(filename, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
