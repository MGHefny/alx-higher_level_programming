#!/usr/bin/node

const callsys = require('fs');
callsys.readFile(process.argv[2], 'utf-8',
  function (errorobject, data) {
    if (errorobject) {
      console.log(errorobject);
      return;
    }
    console.log(data);
  });
