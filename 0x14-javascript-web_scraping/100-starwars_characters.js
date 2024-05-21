#!/usr/bin/node
const reqq = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
reqq.get(url, (errorobject, respo, thebody) => {
  if (errorobject) {
    console.log(errorobject);
  } else {
    const chars = JSON.parse(thebody).chars;
    for (const charr of chars) {
      reqq.get(charr, (errorobject, respo, thebody) => {
        if (errorobject) {
          console.log(errorobject);
        } else {
          console.log(JSON.parse(thebody).name);
        }
      });
    }
  }
});
