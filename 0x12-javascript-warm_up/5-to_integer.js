#!/usr/bin/node
const { argv } = require('process');
const args = argv.slice(2);
let to_int = parseInt(args, 10);

if (isNaN(to_int)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + to_int);
}
