#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let n = 0; n < this.height; n++) {
      let y = '';
      for (let z = 0; z < this.width; z++) {
        y += c;
      }
      console.log(y);
    }
  }
}
module.exports = Square;
