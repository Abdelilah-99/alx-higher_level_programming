#!/usr/bin/node
const { argv } = require('process');
const args = argv.slice(2);

console.log(args[0] + ' is ' + args[1]);
