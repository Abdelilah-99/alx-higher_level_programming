#!/usr/bin/node
const { argv } = require('process');
const args = argv.slice(2);
const toInt = parseInt(args, 10);

if (isNaN(toInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + toInt);
}
