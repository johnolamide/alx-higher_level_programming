#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
    return;
  }
  todos = JSON.parse(body);
  const completedTasks = {};
  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasks[todo.userId]) {
        completedTasks[todo.userId]++;
      } else {
        completedTasks[todo.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
