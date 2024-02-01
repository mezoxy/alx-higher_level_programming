#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('ERROR!!', error.message);
  } else {
    const userTaskCount = {};
    let numTasks = 0;

    const tasks = JSON.parse(body);

    let currentUserId = tasks[0].userId;

    for (const task of tasks) {
      if (task.userId === currentUserId) {
        if (task.completed) {
          numTasks += 1;
        }
      } else {
        userTaskCount[currentUserId] = numTasks;

        if (task.completed) {
          numTasks = 1;
        } else {
          numTasks = 0;
        }

        currentUserId = task.userId;
      }
    }

    // Include the count for the last user
    userTaskCount[currentUserId] = numTasks;

    console.log(userTaskCount);
  }
});
