#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const file1 = argv[2];
const file2 = argv[3];
const destination = argv[4];

fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) throw err;
  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) throw err;
    fs.writeFile(destination, data1 + data2, (err) => {
      if (err) throw err;
    });
  });
});
