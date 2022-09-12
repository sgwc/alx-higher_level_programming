#!/usr/bin/node
const loopArgs = process.argv[2];
if (!loopArgs) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < loopArgs; x++) {
    console.log('C is fun');
  }
}
