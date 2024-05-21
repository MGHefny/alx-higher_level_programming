#!/usr/bin/node
const reqq = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const idd = process.argv[2];
reqq.get(url + idd, (errorobject, respo, thebody) => {
  if (!errorobject) {
    const cnt = JSON.parse(thebody);
    const chars = cnt.chars;
    for (const chaar of chars) {
      reqq.get(chaar, (errorobject, respo, thebody) => {
        if (errorobject) {
          console.log(errorobject);
        } else {
          const nms = JSON.parse(thebody);
          console.log(nms.name);
        }
      });
    }
  } else {
    console.log(errorobject);
  }
});
