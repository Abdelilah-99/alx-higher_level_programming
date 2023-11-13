#!/usr/bin/node
const args = process.argv.slice(2);
let output = '';

if (args[0] === undefined) {
  console.log('Missing size');
}
for (let index = 0; index < args[0]; index++) {
  for (let index = 0; index < args[0]; index++) {
	  output += 'X';
  }
  if (index != args[0] - 1){
	  output += '\n';
  }
}
if (output != '') {
  console.log(output);
}
