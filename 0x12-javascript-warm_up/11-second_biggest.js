#!/usr/bin/node
const process = require('process');
const arg = process.argv;
if (arg.length < 3) {
  console.log(0);
} else if (arg.length === 3) {
 console.log(0);
} else {
  for (let i = 2; i < arg.length; i++) {
    arg[i] = parseInt(arg[i]);
  }
  arg.shift();
  arg.shift();
  console.log(Math.max(arg));
  arg.splice(arg.indexOf(Math.max(arg)), arg.indexOf(Math.max(arg)));
  console.log(Math.max(arg));
}
