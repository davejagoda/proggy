#!/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Resources/jsc

var dict = {'a': '1',
	    'b': '2',
	    'c': '3'};

print('dict:' + dict);
print('keys:' + Object.keys(dict));

for (var key in dict) {
    print('key:' + key + ' value:' + dict[key]);
}
