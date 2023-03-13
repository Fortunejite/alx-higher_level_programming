#!/usr/bin/node
const process = require('process');
const arg = process.argv;
if (Number.isNaN(parseInt(arg[2]))) {
  console.log('Not a number');
} else {
  console.log(parseInt(arg[2]));
}
