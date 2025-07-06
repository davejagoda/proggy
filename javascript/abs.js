#!/usr/bin/env node

function abs(n) {
  n < 0 ? (n = -n) : n;
  return n;
}

for (var i = -1; i < 2; ++i) {
  console.log(i, abs(i));
}
