#!/usr/bin/node
const map1 = (require('./100-data').list).map((x, y) => x * y);
console.log(require('./100-data').list);
console.log(map1);
