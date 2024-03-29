#!/usr/bin/node
const argv = process.argv;
let max = 0;
let secondMax = 0;

if (argv.length > 2) {
  const args = [];
  for (let i = 2; i < argv.length; i++) {
    args.push(Number(argv[i]));
  }
  max = Math.max(...args);
  if (args.length > 1) {
    const args2 = [];
    for (let i = 0; i < args.length; i++) {
      if (args[i] !== max) {
        args2.push(args[i]);
      }
    }
    secondMax = Math.max(...args2);
  }
}
console.log(secondMax);
