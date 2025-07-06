var casper = require("casper").create({
  //  verbose: true,
  //  logLevel: 'debug',
  pageSettings: {
    userAgent:
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:55.0) Gecko/20100101 Firefox/55.0",
  },
  viewportSize: {
    width: 1440,
    height: 900,
  },
});

var url = "https://cpalo-mt.iii.com/iii/encore/myaccount?lang=eng&suite=def";
var titles;

casper.on("remote.message", function (msg) {
  this.echo("remote message caught: " + msg);
});

casper.on("page.error", function (msg) {
  this.echo("remote error caught: " + msg);
});

var system = require("system");
var password = system.env.PACLPIN;
if (undefined === password) {
  casper.echo("Set PACLPIN environment variable");
  casper.exit(1);
}

if (casper.cli.args.length === 1) {
  var username = casper.cli.args[0];
  var timeout = 0;
  var capture = false;
  var verbose = false;
  if (casper.cli.has("timeout")) timeout = casper.cli.get("timeout");
  if (casper.cli.has("capture")) capture = true;
  if (casper.cli.has("verbose")) verbose = true;
} else {
  casper.echo("Need exactly one arguments: username");
  casper.echo("Option: --timeout=seconds");
  casper.echo("Option: --capture");
  casper.echo("Option: --verbose");
  casper.exit(1);
}

function getTitles() {
  var titles = document.querySelectorAll("span.patFuncTitleMain");
  return Array.prototype.map.call(titles, function (e) {
    return e.getAttribute("text");
  });
}

casper.start(url, function () {
  if (verbose) this.echo("url=" + url + " timeout=" + timeout);
  if (capture) this.capture("home.png");
  this.fillSelectors(
    "form#fm1",
    {
      "input[id = code]": username,
      "input[id = pin]": password,
    },
    true,
  );
  if (capture) this.capture("home_fill.png");
});

casper.then(function () {
  this.waitForSelector("a#patronAccountExternalLinkComponent", function () {
    if (verbose) this.echo(this.getHTML());
    if (capture) this.capture("home_next.png");
    var str = this.getHTML("h2");
    var re = /\s+(.*)\s+/;
    var match = re.exec(str);
    this.echo(match[1]);
  });
});

casper.then(function () {
  if (verbose) this.echo(this.getHTML());
  if (capture) this.capture("catalog.png");
  //  var tags = this.getElementsInfo('span.patFuncTitleMain');
  //  this.echo('number of tags is:' + tags.length);
  //  tags.forEach(function(e) {casper.echo('>' + e.text + '<');})
});

casper.run();
