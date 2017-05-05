#!/usr/bin/env node

// this should take an argument
// what is lstrip and rstrip or strip all whitespace in JavaScript?

var listOfLists = [
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
  console.log(s);
  for (var i = 0; i < lol.length; i++) {
    for (var j = 0; j < lol[i].length; j++) {
      if (s.toUpperCase() === lol[i][j]) {
        return([i,j]);
      }
    }
  }
  return([-1,-1]);
}

console.log('list length:' + listOfLists.length);
for (var i = 0; i < listOfLists.length; i++) {
  console.log(listOfLists[i][0] + ' is ' + listOfLists[i][1] + ' is ' + listOfLists[i][2]);
}

console.log(findIt('WO', listOfLists));
console.log(findIt('wo', listOfLists));
console.log(findIt('ん', listOfLists));
console.log(findIt('a ', listOfLists));
console.log(findIt('日', listOfLists));
