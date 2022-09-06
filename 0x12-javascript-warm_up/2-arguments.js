#!/usr/bin/node

const { argv } = require('process');
const argc = argv.length;

if (argc === 2) {
  console.log('No arguments');
} else if (argc === 3) {
  console.log('Arguments found');
} else {
  console.log('Arguments found');
}
