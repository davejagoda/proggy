#!/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Resources/jsc

// this should take an argument
// what is lstrip and rstrip or strip all whitespace in JavaScript?

listOfLists = [
  ['A ', 'あ', 'ア'],
  ['I ', 'い', 'イ'],
  ['U ', 'う', 'ウ'],
  ['E ', 'え', 'エ'],
  ['O ', 'お', 'オ'],
  ['KA', 'か', 'カ'],
  ['KI', 'き', 'キ'],
  ['KU', 'く', 'ク'],
  ['KE', 'け', 'ケ'],
  ['KO', 'こ', 'コ'],
  ['SA', 'さ', 'サ'],
  ['SI', 'し', 'シ'],
  ['SU', 'す', 'ス'],
  ['SE', 'せ', 'セ'],
  ['SO', 'そ', 'ソ'],
  ['TA', 'た', 'タ'],
  ['TI', 'ち', 'チ'],
  ['TU', 'つ', 'ツ'],
  ['TE', 'て', 'テ'],
  ['TO', 'と', 'ト'],
  ['NA', 'な', 'ナ'],
  ['NI', 'に', 'ニ'],
  ['NU', 'ぬ', 'ヌ'],
  ['NE', 'ね', 'ネ'],
  ['NO', 'の', 'ノ'],
  ['HA', 'は', 'ハ'],
  ['HI', 'ひ', 'ヒ'],
  ['HU', 'ふ', 'フ'],
  ['HE', 'へ', 'ヘ'],
  ['HO', 'ほ', 'ホ'],
  ['MA', 'ま', 'マ'],
  ['MI', 'み', 'ミ'],
  ['MU', 'む', 'ム'],
  ['ME', 'め', 'メ'],
  ['MO', 'も', 'モ'],
  ['YA', 'や', 'ヤ'],
  ['YU', 'ゆ', 'ユ'],
  ['YO', 'よ', 'ヨ'],
  ['RA', 'ら', 'ラ'],
  ['RI', 'り', 'リ'],
  ['RU', 'る', 'ル'],
  ['RE', 'れ', 'レ'],
  ['RO', 'ろ', 'ロ'],
  ['WA', 'わ', 'ワ'],
  ['WI', 'ゐ', 'ヰ'],
  ['WE', 'ゑ', 'ヱ'],
  ['WO', 'を', 'ヲ'],
  ['N ', 'ん', 'ン']
];

function findIt(s, lol) {
  print(s);
  for (var i = 0; i < lol.length; i++) {
    for (var j = 0; j < lol[i].length; j++) {
      if (s.toUpperCase() === lol[i][j]) {
        return([i,j]);
      }
    }
  }
  return([-1,-1]);
}

print('list length:' + listOfLists.length);
for (var i = 0; i < listOfLists.length; i++) {
  print(listOfLists[i][0] + ' is ' + listOfLists[i][1] + ' is ' + listOfLists[i][2]);
}

print(findIt('WO', listOfLists));
print(findIt('wo', listOfLists));
print(findIt('ん', listOfLists));
print(findIt('a', listOfLists));
