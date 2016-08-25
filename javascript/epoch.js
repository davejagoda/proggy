#!/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Resources/jsc

function main() {
    var zero_epoch = new Date(0);
    var curr_epoch = new Date();
    print('0000000000',                zero_epoch.toISOString());
    print(Math.floor(curr_epoch/1000), curr_epoch.toISOString());
}

main();
