#!/usr/bin/node
const reqq = require('request');
reqq.get(process.argv[2], { json: true }, (errorobject, respo, thebody) => {
  if (errorobject) {
    console.log(errorobject);
    return;
  }
  const tsksComp = {};
  thebody.forEach((dn) => {
    if (dn.completed) {
      if (!tsksComp[dn.userId]) {
        tsksComp[dn.userId] = 1;
      } else {
        tsksComp[dn.userId] += 1;
      }
    }
  });
  console.log(tsksComp);
});
