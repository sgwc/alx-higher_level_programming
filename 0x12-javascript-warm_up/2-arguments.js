#!/usr/bin/node
const allArgs = process.argv;
if (allArgs.length < 3) {
  console.log('No arguments');
} else {
  console.log('Arguments found');
}
