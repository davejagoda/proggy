#!/usr/bin/env node

let uris = ['http://localhost:8000', 'http://davejagoda.nfshost.com',
            'http://www.google.com', 'http://www.yahoo.com']
let request = require('request');

for (let uri of uris) {
  console.log('about to request:' + uri);
  request(uri, function callback(error, response, body) {
    console.log('in callback:' + uri);
    if (error) console.log('error:', error);
    if (response) console.log('statusCode:', response.statusCode);
    if (body) console.log('body length:', body.length);
  });
}
