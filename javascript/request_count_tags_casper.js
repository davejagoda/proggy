var casper = require("casper").create();

casper.on("remote.message", function (msg) {
  this.echo("remote message caught: " + msg);
});

casper.on("page.error", function (msg) {
  this.echo("remote error caught: " + msg);
});

if (casper.cli.args.length === 2) {
  var url = casper.cli.args[0];
  var tag = casper.cli.args[1];
  var selector = "";
  var timeout = 0;
  var verbose = false;
  if (casper.cli.has("selector")) selector = casper.cli.get("selector");
  if (casper.cli.has("timeout")) timeout = casper.cli.get("timeout");
  if (casper.cli.has("verbose")) verbose = true;
} else {
  casper.echo("Need exactly two arguments: url and tag");
  casper.echo("Option: --selector=#id or .class");
  casper.echo("Option: --timeout=seconds");
  casper.echo("Option: --verbose");
  casper.echo(
    "Tip: if you want to count just the tags that match the query selector",
  );
  casper.echo("     supply tag as tag.class or tag#id");
  casper.echo("     since it waits for tag+selector and counts tag");
  casper.exit(1);
}

casper.start(url, function () {
  if (verbose)
    this.echo(
      "url=" +
        url +
        " tag=" +
        tag +
        " selector=" +
        selector +
        " timeout=" +
        timeout,
    );
  // wait until a tag with the selector is present
  this.waitForSelector(tag + selector, function () {
    this.echo("found: " + tag + selector);
  });
  // wait timeout seconds for the page to load
  this.wait(timeout * 1000, function () {
    var tags = [];
    if (this.exists(tag)) tags = this.getElementsInfo(tag);
    this.echo("number of tags of type:" + tag + " is " + tags.length);
    tags.forEach(function (e) {
      casper.echo(">" + e.text + "<");
    });
  });
});

casper.then(function () {
  var ret_val = this.evaluate(
    function (tag, selector) {
      var results = [];
      var qs = document.querySelectorAll(tag + selector);
      for (var i = 0, max = qs.length; i < max; i++) {
        results.push(qs[i].innerText);
      }
      return results;
    },
    tag,
    selector,
  );
  this.echo("this.evaluate");
  this.echo("number of tags of type:" + tag + " is " + ret_val.length);
  ret_val.forEach(function (e) {
    casper.echo(">" + e + "<");
  });
});

casper.run();
