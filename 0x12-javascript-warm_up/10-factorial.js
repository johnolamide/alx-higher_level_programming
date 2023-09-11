#!/usr/bin/node
const argv = process.argv;
const num = Number(argv[2]);

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(num));
