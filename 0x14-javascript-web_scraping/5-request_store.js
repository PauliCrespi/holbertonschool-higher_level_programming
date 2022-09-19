#!/usr/bin/node
const filmurl = String(process.argv[2]);
const filename = String(process.argv[3]);
const axios = require('axios');
const fs = require('fs');

axios
  .get(filmurl)
  .then((response) => {
    const content = response.data;
    fs.writeFile(filename, content, err => {
      if (err) {
        console.error(err);
      }
    });
  })
  .catch(error => {
    console.error(`code: ${error.response.status}`);
  });
