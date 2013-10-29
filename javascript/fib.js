#!/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Resources/jsc

function fib(n) {
    if (n < 2) { return n; }
    else { return fib(n-1) + fib(n-2); }
}

for (i = 0; i < 40; i++) {
    print(i, fib(i));
}
