#!/usr/bin/node
const loopArgs = process.argv[2];
if (!parseInt(loopArgs)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < loopArgs; x++) {
    console.log('X'.repeat(loopArgs));
  }
}
