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
  arg.sort(function(a, b){return a - b});
  console.log(arg[arg.length - 2]);
}
