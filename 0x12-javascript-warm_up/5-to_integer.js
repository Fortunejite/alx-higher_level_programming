#!/usr/bin/node
const process = require('process');
const arg = process.argv;
if (isNaN(arg[2])) {
  console.log('Not a number');
} else {
  console.log(parseInt(arg[2]));
}