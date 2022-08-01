#!/usr/bin/node
const args = process.argv;
if (args[2] === undefined) {
  console.log('0');
} else if (args[2] === '1') {
  console.log('0');
} else {
  let aux = process.argv[2];
  for (let i = 0; i <= args.length; i++) {
    if (args[i] > aux) {
      aux = args[i];
    }
  }
  let temp = process.argv[2];
  for (let j = 0; j <= args.length; j++) {
    if (args[j] > temp && args[j] < aux) {
      temp = args[j];
    }
  }
  console.log(temp);
}
