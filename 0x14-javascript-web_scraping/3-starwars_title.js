#!/usr/bin/node
const request = require('request');
const num = process.argv[2];
request('http://swapi.co/api/films/' + num, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
