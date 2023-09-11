#!/usr/bin/node
const argv = process.argv;
const occurence = Number(argv[2]);
const message = 'C is fun';

if (isNaN(occurence)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < occurence; i++) {
    console.log(`${message}`);
  }
}
