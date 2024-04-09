#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const c = Number(process.argv[2]);
  let x = 0;
  while (x < c) {
    console.log('c'.repeat(c));
    x++;
  }
}
