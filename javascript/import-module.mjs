#!/usr/bin/env node --experimental-modules

console.log("begin");
import { square, cube } from "./module.mjs";
for (var i = 0; i < 3; i++) {
  console.log(i, square(i), cube(i));
}
console.log("end");
