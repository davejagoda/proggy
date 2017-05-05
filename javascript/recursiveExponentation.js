#!/usr/bin/env node

function power(base, exponent) {
  if (exponent == 0)
    return 1;
  else
    return base * power(base, exponent - 1);
}

console.log(power(2,0));
console.log(power(2,1));
console.log(power(2,10));
console.log(power(2,100));
console.log(power(2,1000));
console.log(power(2,10000));
console.log(power(2,37299));
console.log(power(2,37300));
console.log(power(2,37301));
