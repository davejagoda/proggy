#!/usr/bin/env python2

# do not convert this to python3

english_a = chr(97)
print(english_a, type(english_a))

hiragana_a = unichr(0x3042)
print(hiragana_a, type(hiragana_a))

letters = [english_a, hiragana_a.encode('utf-8')]

print('this will work')
print(''.join(letters))
print('this will not')
print(u''.join(letters))
