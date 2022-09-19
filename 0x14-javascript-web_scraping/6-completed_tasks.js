#!/usr/bin/node
const filmurl = String(process.argv[2]);
const axios = require('axios');

axios
  .get(filmurl)
  .then((response) => {
    const list = {};
    for (const users of response.data) {
      if (users.completed) {
        if (users.userId in list) {
          list[users.userId]++;
        } else {
          list[users.userId] = 1;
        }
      }
    }
    console.log(list);
  })
  .catch(error => {
    console.error(`code: ${error.response.status}`);
  });
