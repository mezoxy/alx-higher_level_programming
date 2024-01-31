#!/usr/bin/node
const req = require('request');

req(process.argv[2], function (err, response, body) {
  if (err) {
    console.log('ERROR!!');
  } else {
    const dic = {};
    let NumTask = 0;
    const tasks = JSON.parse(body);
    let UsrId = tasks[0].userId;
    for (const task of tasks) {
	    if (task.userId === UsrId) {
		    if (task.completed === true) {
			    NumTask += 1;
		    }
	    } else {
		    dic[UsrId] = NumTask;
		    if (task.completed === true) {
			    NumTask = 1;
		    } else {
			    NumTask = 0;
		    }
		    UsrId = task.userId;
	    }
    }
    dic[UsrId] = NumTask;
    console.log(dic);
  }
});
