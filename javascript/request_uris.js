#!/usr/bin/env node

const uris = [
  "http://localhost:8000",
  "http://davejagoda.nfshost.com",
  "http://www.google.com",
  "http://www.yahoo.com",
];
const axios = require("axios");

for (let uri of uris) {
  console.log("about to request:" + uri);
  axios
    .get(uri)
    .then(function (response) {
      console.log("response:" + response.status);
      console.log("body length:" + response.data.length);
    })
    .catch(function (error) {
      console.log("error:" + error);
    })
    .finally(function () {
      console.log("finished:" + uri);
    });
}
