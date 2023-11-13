#!/usr/bin/node
const args = process.argv.slice(2);
const a = parseInt(args[0], 10);
const b = parseInt(args[1], 10);

add(a, b);
function add (a, b) {
  console.log(a + b);
}
