#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/';
const filmurl = url.concat(String(process.argv[2]), '/');
const axios = require('axios');

axios
  .get(filmurl)
  .then(res => {
    console.log(res.data.title);
  })
  .catch(error => {
    console.error(error);
  });
