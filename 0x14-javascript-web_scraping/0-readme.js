#!/usr/bin/node

const callsys = require('fs');
callsys.readFile(process.argv[2], 'utf-8',
  function (error_object, data) {
    if (error_object) {
      console.log(error_object);
      return;
    }
    console.log(data);
  });
