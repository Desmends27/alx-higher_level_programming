#!/usr/bin/node
let current = 0;

exports.logMe = function (item) {
  function log () {
    console.log(`${current}: ${item}`);
    current++;
  }
  log();
};
