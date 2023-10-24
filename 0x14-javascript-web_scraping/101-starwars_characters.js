#!/usr/bin/node

const request = require('request');
const async = require('async');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
    return;
  }
  const movie = JSON.parse(body);
  const characters = movie.characters;

  async.eachSeries(characters, (characterUrl, callback) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('error:', error);
        callback();
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
      callback();
    });
  });
});
