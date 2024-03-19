#!/usr/bin/node

const { argv } = require('node:process');
const num = argv[2];

if (!num) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
