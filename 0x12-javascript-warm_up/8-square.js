#!/usr/bin/node
const { argv } = require('node:process');
const number = argv[2];

if (!number) {
  console.log('Missing size');
}
for (let i = 0; i < number; i++) {
  let x = '';
  for (let j = 0; j < number; j++) {
    x += 'X';
  }
  console.log(x);
}
