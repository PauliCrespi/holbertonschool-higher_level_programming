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
  console.log(aux);
}
