#!/usr/bin/node
const process = require('process');
const arg = process.argv;
if (isNaN(arg[2])) {
  console.log('Missing size');
} else {
  const num = parseInt(arg[2]);
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
