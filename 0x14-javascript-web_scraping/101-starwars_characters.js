#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

getRequest(url).then(movie => {
  const characters = movie.characters;
  let promiseChain = Promise.resolve();

  characters.forEach(characterUrl => {
    promiseChain = promiseChain.then(() => getRequest(characterUrl))
      .then(character => console.log(character.name));
  });
}).catch(console.error);
