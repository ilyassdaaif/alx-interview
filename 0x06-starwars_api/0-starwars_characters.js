#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

function fetchCharacter(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request(apiUrl, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  try {
    const characterNames = await Promise.all(characterUrls.map(fetchCharacter));
    characterNames.forEach(name => console.log(name));
  } catch (err) {
    console.error('Error fetching characters:', err);
  }
});
