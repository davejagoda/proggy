#!/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Resources/jsc

function abs(n) {
    print(n);
    (n < 0) ? n = -n : n = n;
    return n;
}

print(abs(0));
print(abs(1));
print(abs(-1));
