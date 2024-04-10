#!/usr/bin/node
exports.esrever = function (list) {
  let x = list.length - 1;
  let n = 0;
  while ((x - n) > 0) {
    const aux = list[x];
    list[x] = list[n];
    list[n] = aux;
    n++;
    x--;
  }
  return list;
};
