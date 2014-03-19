#!/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Resources/jsc

function power(base, exponent) {
    if (exponent == 0)
	return 1;
    else
	return base * power(base, exponent - 1);
}

print(power(2,0));
print(power(2,1));
print(power(2,10));
print(power(2,100));
print(power(2,1000));
print(power(2,10000));
print(power(2,37299));
print(power(2,37300));
print(power(2,37301));
