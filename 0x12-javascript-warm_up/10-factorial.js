#!/usr/bin/node
const args = process.argv;
const numb = parseInt(args[2]);
function factorialize (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 1) {
    return 1;
  } else {
    return (num * factorialize(num - 1));
  }
}
console.log(factorialize(numb));
