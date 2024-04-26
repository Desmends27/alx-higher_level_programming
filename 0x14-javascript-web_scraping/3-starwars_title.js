#!/usr/bin/node
const request = require('request');
const process = require('process');

const num = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + num;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const filmData = JSON.parse(body);
  console.log(filmData.title);
});
