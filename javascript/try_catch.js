#!/usr/bin/env node

var good_json = "[]";
var bad_json = "<!DOCTYPE HTML>";

function main() {
  try {
    JSON.parse(good_json);
    console.log("parsed good_json");
    JSON.parse(bad_json);
    console.log("parsed bad_json");
  } catch (error) {
    console.log(`got an exception while parsing JSON: ${error}`);
  }
}

main();
console.log("returned from main()");
