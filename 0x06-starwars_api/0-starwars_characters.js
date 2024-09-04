#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;
  const characterNames = [];
  let requestsCompleted = 0;

  characters.forEach((characterUrl, index) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      const character = JSON.parse(charBody);
      characterNames[index] = character.name;
      requestsCompleted++;

      // Only print characters when all requests have completed
      if (requestsCompleted === characters.length) {
        characterNames.forEach(name => console.log(name));
      }
    });
  });
});
