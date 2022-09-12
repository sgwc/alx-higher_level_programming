#!/usr/bin/node
const allArgs = process.argv[2];
if (!allArgs) {
  console.log('No argument');
} else {
  console.log(allArgs);
}
