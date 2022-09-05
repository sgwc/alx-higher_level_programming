#!/usr/bin/node
const allArgs = process.argv[2];
if (!allArgs) {
  console.log('No arguments');
} else {
  console.log(allArgs);
}
