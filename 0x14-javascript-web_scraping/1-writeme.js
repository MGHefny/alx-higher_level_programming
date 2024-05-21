#!/usr/bin/node
const callsys = require('fs');
callsys.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (errorobject) {
    if (errorobject) {
      console.log(errorobject);
    }
  });
