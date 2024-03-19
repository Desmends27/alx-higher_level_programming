#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length - 2 <= 0) {
  console.log('No arguemnt');
} else if (argv.length - 2 === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
