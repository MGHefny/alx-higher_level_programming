#!/usr/bin/node
const reqq = require('request');
const url = process.argv[2];
reqq.get(url, function (errorobject, respo) {
  if (errorobject) {
    console.log(errorobject);
  } else {
    console.log('code: ' + respo.statusCode);
  }
});
