#!/usr/bin/env coffee

fib = (n) ->
  if n < 2
    n
  else
    fib(n-1) + fib(n-2)

log = (n, f) ->
  console.log(n + ':' + f)

if 3 == process.argv.length
  log(process.argv[2], fib(process.argv[2]))
else
  i = 0
  log(i, fib(i++)) while i >= 0
