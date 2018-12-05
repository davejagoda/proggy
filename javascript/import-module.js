#!/usr/bin/env node

console.log('begin');
const {square, cube} = require('./module');
for (var i = 0; i < 3; i++) {
  console.log(i, square(i), cube(i));
}
console.log('end');
