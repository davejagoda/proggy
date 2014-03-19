#!/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Resources/jsc

// this kills Safari

function chicken(arg) {
  print("chicken:" + ++arg);
  return egg(arg);
}

function egg(arg) {
  print("egg:" + ++arg);
  return chicken(arg);
}

print(chicken(0) + " came first.");
