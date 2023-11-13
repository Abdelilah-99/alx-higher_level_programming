#!/usr/bin/node
const { argv } = require('process');
const Len = argv.length;

if (Len === 2) {
	console.log('No argument');
} else if (Len === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
