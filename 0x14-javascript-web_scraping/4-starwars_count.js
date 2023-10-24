#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
    if (error) {
        console.error('error:', error);
        return;
    }
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      if (film.characters.includes(characterId)) {
        count++
      }
    });
    console.log(count);
});

