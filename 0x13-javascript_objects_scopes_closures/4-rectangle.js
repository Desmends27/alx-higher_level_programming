#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w !== 0 && h !== 0 && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (letter = 'X') {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += letter;
      }
      console.log(x);
    }
  }

  rotate () {
    [[this.width], [this.height]] = [[this.height], [this.width]];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
