#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const i of list) {
    if (searchElement === i) {
      occurences++;
    }
  }
  return occurences;
};
