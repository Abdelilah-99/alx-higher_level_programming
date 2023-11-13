#!/usr/bin/node
const { argv } = require('process');
const args = argv.slice(2);
const toInt = parseInt(args, 10);
let output = '';

if (toInt === undefined || isNaN(toInt)) {
  console.log('Missing size');
}
for (let index = 0; index < toInt; index++) {
  for (let index = 0; index < toInt; index++) {
    output += 'X';
  }
  if (index !== toInt - 1) {
    output += '\n';
  }
}
if (output !== '') {
  console.log(output);
}
