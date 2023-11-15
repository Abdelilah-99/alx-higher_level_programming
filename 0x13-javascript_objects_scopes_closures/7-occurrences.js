#!/usr/bin/node

exports.nbOccurences = function nbOccurences (arr, idx) {
  let count = 0;
  for (let index = 0; index < arr.length; index++) {
    if (arr[index] === idx) {
      count++;
    }
  }
  return count;
}
