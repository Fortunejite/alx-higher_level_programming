#!/usr/bin/node
const process = require('process');
const arg = process.argv;
num = parseInt(arg[2]);
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 1) {
    return 1;
  }
  return(a * factorial(a - 1));
}
console.log(factorial(num));
