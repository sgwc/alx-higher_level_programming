#!/usr/bin/node

function fact (n) {
  if (!n) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

const { argv } = require('process');
const num = parseInt(argv[2]);

console.log(fact(num));
