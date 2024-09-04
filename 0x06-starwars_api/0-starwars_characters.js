#!/usr/bin/node
// Prints all characters of a Star Wars movie

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

  characters.forEach(characterUrl => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
	console.error(charError);
	return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
