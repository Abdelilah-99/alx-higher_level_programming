#!/usr/bin/node
const { argv } = require('process');
const largs = argv.length;

if (largs === 2) {
	console.log('No argument');
} else if (largs === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
