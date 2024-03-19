#!/usr/bin/node
const { argv } = require('node:process');

function factorial (number) {
  if (number <= 0) {
    return 0;
  }
  if (number === 1) {
    return 1;
  }
  return number * factorial(number - 1);
}

const number = Number(argv[2]);
if (number) {
  console.log(factorial(number));
}
