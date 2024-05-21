#!/usr/bin/node
const reqq = require('request');
const callsys = require('fs');
reqq.get(process.argv[2], (errorobject, respo, thebody) => {
  if (!errorobject) {
    callsys.writeFile(process.argv[3], thebody, 'utf-8', (errorobject) => {
      if (errorobject) {
        console.log(errorobject);
      }
    });
  } else {
    console.log(errorobject);
  }
});
