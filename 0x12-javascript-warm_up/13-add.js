#!/usr/bin/node
exports.add = (a, b) => a + b;
const add = require('./13-add').add;
console.log(add(3, 5));
