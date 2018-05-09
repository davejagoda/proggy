#!/usr/bin/env python3

import unicodedata

def make_list(lo, hi):
# risuto is Romaji for list, since lower case l is easily confused
# it is a list of pairs (tuples) like this: (romaji, kana)
    risuto = []
    for i in range(lo,hi):
        kana = chr(i)
        try:
            name = unicodedata.name(kana)
        except:
            name = 'NONE'
        if '' == unicodedata.decomposition(kana) and 'LETTER' in name and 'SMALL' not in name:
            (syllabary, letter, romaji) = name.split(' ')
            if 1 == len(romaji): romaji += ' ' # hack, do this with format
            risuto.append((romaji, kana))
    return(risuto)

if '__main__' == __name__:
    hiragana = make_list(0x3040,0x30a0)
    katakana = make_list(0x30a0,0x3100)
    assert(len(hiragana) == len(katakana))
    for i in range(len(hiragana)):
        assert(hiragana[i][0] == katakana[i][0])
        print('{}:{}:{}'.format(hiragana[i][0], hiragana[i][1], katakana[i][1]))
