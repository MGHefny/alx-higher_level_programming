#!/usr/bin/node
const reqq = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const idd = process.argv[2];
reqq.get(url + idd, (errorobject, respo, thebody) => {
  if (errorobject) {
    console.log(errorobject);
  } else {
    console.log(JSON.parse(thebody).title);
  }
});
