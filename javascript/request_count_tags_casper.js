var casper = require('casper').create();

if (casper.cli.args.length === 2) {
    var url = casper.cli.args[0];
    var tag = casper.cli.args[1];
    if (casper.cli.has('selector')) {
        var selector = casper.cli.get('selector');
    } else {
        var selector = '';
    }
    if (casper.cli.has('timeout')) {
        var timeout = casper.cli.get('timeout');
    } else {
        var timeout = 0;
    }
    if (casper.cli.has('verbose')) {
        var verbose = true;
    } else {
        var verbose = false;
    }
} else {
    casper.echo('Need exactly two arguments: url and tag');
    casper.echo('Option: --selector=#id or .class');
    casper.echo('Option: --timeout=seconds');
    casper.echo('Option: --verbose');
    casper.echo('Tip: if you want to count just the tags that match the query selector');
    casper.echo('     supply tag as tag.class or tag#id');
    casper.echo('     since it waits for tag+selector and counts tag');
    casper.exit(1);
}

casper.start(url, function() {
    if (verbose) {
        this.echo('url=' + url + ' tag=' + tag + ' selector=' + selector + ' timeout=' + timeout);
    }
    // wait until a tag with the selector is present
    this.waitForSelector(tag + selector, function() {
        this.echo('found: ' + tag + selector);
    });
    // wait timeout seconds for the page to load
    this.wait(timeout * 1000, function() {
        var tags = [];
        if (this.exists(tag)) {
            tags = this.getElementsInfo(tag);
        }
        this.echo('number of tags of type:' + tag + ' is ' + tags.length);
    });
});

casper.run();
