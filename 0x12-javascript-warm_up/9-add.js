#!/usr/bin/node
const argv = process.argv;
const first = Number(argv[2]);
const second = Number(argv[3]);

function add (a, b) {
  const result = a + b;
  return result;
}

const result = add(first, second);
console.log(`${result}`);
