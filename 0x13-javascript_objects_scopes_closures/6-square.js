#!/usr/bin/node
const ASquare = require('./5-square');

class Square extends ASquare {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c) {
      for (let index = 0; index < this.height; index++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
