var casper = require('casper').create();

if (casper.cli.args.length === 2) {
    var url = casper.cli.args[0];
    var tag = casper.cli.args[1];
} else {
    casper.echo('Need exactly two arguments: url and tag').exit();
}

casper.start(url, function() {
    var tags = [];
    if (this.exists(tag)) {
        tags = this.getElementsInfo(tag);
    }
    this.echo('number of tags of type:' + tag + ' is ' + tags.length);
});

casper.run();
