#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
function fetchFilm (id) {
  return new Promise((resolve, reject) => {
    request('https://swapi-api.alx-tools.com/api/films/' + id, (error, response, body) => {
      if (error) {
        reject(new Error('error occured'));
      } else if (response && response.statusCode === 200) {
        const list = JSON.parse(body).characters;
        resolve(list);
      } else {
        reject(new Error(response.statusCode));
      }
    });
  });
}

function fetchName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(new Error('error occured'));
      } else if (response && response.statusCode === 200) {
        const actorName = JSON.parse(body).name;
        resolve(actorName);
      } else {
        reject(new Error(response.statusCode));
      }
    });
  });
}

async function printName () {
  try {
    const list = await fetchFilm(id);
    for (const url of list) {
      const charName = await fetchName(url);
      console.log(charName);
    }
  } catch (error) {
    console.log(error);
  }
}
printName();
