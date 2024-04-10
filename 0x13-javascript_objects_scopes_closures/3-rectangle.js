#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      let y = '';
      for (let z = 0; z < this.width; z++) {
        y += 'X';
      }
      console.log(y);
    }
  }
}
module.exports = Rectangle;
