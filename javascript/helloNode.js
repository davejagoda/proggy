var http = require('http');
var port = 8080
var data = '<!doctype html>\n<html>\n<head>\n<title>hello</title>\n<meta charset="utf-8" />\n</head>\n<body>\n<b>hello</b>\n</body>\n</html>\n'

http.createServer(function (req, res) {
  console.log('url: ' + req.url);
  console.log('headers:');
  console.log(req.headers);
  res.writeHead(200, {'Content-Type': 'html'});
  res.end(data);
}).listen(port);

console.log('server listening on port:' + port);
