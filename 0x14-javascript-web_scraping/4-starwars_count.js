#!/usr/bin/node
const request = require('request');
const process = require('process');

const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const count = filmData.results.reduce((total, movie) => {
    const hasCharacter = movie.characters.some(character => character.endsWith('/18/'));
    return hasCharacter ? total + 1 : total;
  }, 0);

  console.log(count);
});
