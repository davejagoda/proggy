#!/usr/bin/env node

process.argv.forEach(function (value, index, array) {
  console.log("argument #" + index + " was: " + value);
});
