#!/usr/bin/env node

function main() {
  var curr_epoch = new Date();
  console.log('0000000000'                + ' ' + (new Date(0)).toISOString());
  console.log(Math.floor(curr_epoch/1000) + ' ' + curr_epoch.toISOString());
}

main();
