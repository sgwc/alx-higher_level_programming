#!/usr/bin/node
const allArgs = process.argv;
if (allArgs[2] === undefined) {
  console.log('No arguments');
} else {
  console.log(allArgs[2]);
}
