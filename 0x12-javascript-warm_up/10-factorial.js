#!/usr/bin/node
const process = require('process');
const arg = process.argv;
const num = parseInt(arg[2]);
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 1) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}
console.log(factorial(num));
