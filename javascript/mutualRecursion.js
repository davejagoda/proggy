#!/usr/bin/env node

// this kills Safari

function chicken(arg) {
  console.log("chicken:" + ++arg);
  return egg(arg);
}

function egg(arg) {
  console.log("egg:" + ++arg);
  return chicken(arg);
}

console.log(chicken(0) + " came first.");
