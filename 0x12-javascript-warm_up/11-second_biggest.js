#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 3) {
  console.log(0);
} else {
  let arr = [];
  for (let i = 0; i < args.length; i++) {
    const toint = parseInt(args[i], 10);
    arr = sortedfct(toint, arr);
  }
  console.log(arr[arr.length - 2]);
}
function sortedfct (toint, arr) {
  let inserted = false;
  for (let i = 0; i < arr.length; i++) {
    if (toint < arr[i]) {
      arr.splice(i, 0, toint);
      inserted = true;
      break;
    }
  }
  if (!inserted) {
    arr.push(toint);
  }
  return arr;
}
