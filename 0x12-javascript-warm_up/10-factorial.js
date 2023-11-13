#!/usr/bin/node
const args = process.argv.slice(2);
const n = parseInt(args[0], 10);
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(n));
}
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
