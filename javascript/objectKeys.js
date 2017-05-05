#!/usr/bin/env node

var dict = {'a': '1',
            'b': '2',
            'c': '3'};

console.log('dict:' + dict);
console.log('keys:' + Object.keys(dict));

for (var key in dict) {
  console.log('key:' + key + ' value:' + dict[key]);
}
