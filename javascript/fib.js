#!/usr/bin/env node

function fib(n) {
  if (n < 2) { return n; }
  else { return fib(n-1) + fib(n-2); }
}

for (var i = 0; i < 40; i++) {
  console.log(i, fib(i));
}
