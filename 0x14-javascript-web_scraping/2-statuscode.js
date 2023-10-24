#!/usr/bin/node

request = require('request');
url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
