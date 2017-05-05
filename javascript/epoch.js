#!/usr/bin/env node

function main() {
  var zero_epoch = new Date(0);
  var curr_epoch = new Date();
  console.log('0000000000'                + ' ' + zero_epoch.toISOString());
  console.log(Math.floor(curr_epoch/1000) + ' ' + curr_epoch.toISOString());
}

main();
