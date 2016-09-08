var casper = require('casper').create();

if (casper.cli.args.length === 2) {
    var url = casper.cli.args[0];
    var tag = casper.cli.args[1];
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
    casper.echo('Option: --timeout=#seconds');
    casper.echo('Option: --verbose');
    casper.exit(1);
}

casper.start(url, function() {
    if (verbose) {
        this.echo('url=' + url + ' tag=' + tag + ' timeout=' + timeout);
    }
    this.wait(timeout * 1000, function() {
        var tags = [];
        if (this.exists(tag)) {
            tags = this.getElementsInfo(tag);
        }
        this.echo('number of tags of type:' + tag + ' is ' + tags.length);
    });
});

casper.run();
