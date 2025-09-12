#!/usr/bin/env node

import { readFile } from 'node:fs';

if (3 !== process.argv.length) {
  console.log("Provide exactly one argument: a file to read");
  process.exit(1);
}

const file = process.argv[2];
let uniq = {};

readFile(file, "utf8", function (err, data) {
  if (err) {
    return console.log(err);
  }
  data.split("\n").forEach(function (entry) {
    console.log(entry);
    uniq[entry] = uniq[entry] + 1 || 1;
  });
  console.log(uniq);
});
