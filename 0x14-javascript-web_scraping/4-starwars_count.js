#!/usr/bin/node
const reqq = require('request');
let x = 0;
reqq.get(process.argv[2], (errorobject, respo, thebody) => {
  if (!errorobject) {
    const content = JSON.parse(thebody);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          x += 1;
        }
      });
    });
    console.log(x);
  } else {
    console.log(errorobject);
  }
});
