#!/usr/bin/node
const { argv } = require('node:process');

const list = [];
for (let i = 2; i < argv.length; i++) {
  list.push(Number(argv[2]));
}
list.sort();
if (list.length < 2) {
  console.log(0);
} else {
  console.log(list[list.length - 2]);
}
