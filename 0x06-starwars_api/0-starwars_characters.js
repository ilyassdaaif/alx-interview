#!/usr/bin/node
// Prints all characters of a Star Wars movie.

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Fetch movie data first
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Create an array of promises for each character request
  const characterPromises = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
	  reject(charError);
	} else {
	  const character = JSON.parse(charBody);
	  resolve(character.name);
        }
      });
    });
  });

  // Wait for all character requests to complete
  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(err => console.error(err));
});
