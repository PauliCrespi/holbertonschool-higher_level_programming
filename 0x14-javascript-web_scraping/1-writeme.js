#!/usr/bin/node
const fs = require('fs');
const filename = String(process.argv[2]);
const content = String(process.argv[3]);

fs.writeFile(filename, content, err => {
  if (err) {
    console.error(err);
  }
  // file written successfully
});
