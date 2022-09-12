#!/usr/bin/node
const filmurl = String(process.argv[2]);
const axios = require('axios');

axios
  .get(filmurl)
  .then((response) => {
    let count = 0;
    for (const tittles of response.data.results) {
      for (const vipchar of tittles.characters) {
        if (vipchar === 'https://swapi-api.hbtn.io/api/people/18/') {
          count = count + 1;
        }
      }
    }
    console.log(count);
  })
  .catch(error => {
    console.log('code': error.response.status);
  });
