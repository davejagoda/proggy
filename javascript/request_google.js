#!/usr/bin/env node

var uri = 'http://www.google.com'
var request = require('request');
request(uri, function(error, response, body) {
  if (error) console.log('error:', error);
  if (response) console.log('statusCode:', response.statusCode);
  if (body) console.log('body length:', body.length);
});
