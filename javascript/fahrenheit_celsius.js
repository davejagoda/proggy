#!/usr/bin/env node

function pad (str, len) {
  while (str.length < len) str = ' ' + str;
  return str;
}
var lower =   0; /* lower limit of temperature table */
var upper = 300; /* upper limit of temperature table */
var step  =  20; /* step size */
var fahr = lower;
while (fahr <= upper) {
  var celsius = (5.0/9.0) * (fahr-32.0);
  console.log(pad(fahr.toFixed(),3), pad(celsius.toFixed(1),6));
  fahr = fahr + step;
}
