#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < num; i++) {
  console.log('#'.repeat(num));
}
