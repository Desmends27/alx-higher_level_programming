#!/usr/bin/node
const request = require('request');
const process = require('process');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const tasksDone = {};
  const todos = JSON.parse(body);

  for (const task of todos) {
    if (task.completed === true) {
      if (!tasksDone[task.userId]) {
        tasksDone[task.userId] = 1;
      } else {
        tasksDone[task.userId]++;
      }
    }
  }
  console.log(tasksDone);
}
);
