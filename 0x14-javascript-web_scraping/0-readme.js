#!/usr/bin/node
<<<<<<< HEAD

const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf8', function (err, data = err) {
  console.log(data);
=======
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
>>>>>>> a779e66ddebae797065002fe7ced4e18e68ee403
});
