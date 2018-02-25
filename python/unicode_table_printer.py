#!/usr/bin/env python3

import unicodedata
import urllib.parse

#def get_unicode_using_unicode_escape(n):
#    s = "%x" % n
#    return ('\U' + s.zfill(8)).decode('unicode-escape')

def print_unicode_entry(n):
#    if n > 0xffff:
#        u = get_unicode_using_unicode_escape(n)
#    else:
#        u = unichr(n)
    u = chr(n)
    category = unicodedata.category(u)
    name = unicodedata.name(u, 'unicodedata has no name defined')
    if 'Cs' == category:
        q = ''
        u = '<U+{:x}>'.format(n) # surrogate
    else:
        q = urllib.parse.quote(u)
    print(('{:7d} {:6x} {:12} {} {} {}'.format(n, n, q, u, category, name)))

# you'll get this error if you try to pipe the output to 'more' or to a file
# without encoding the unicode string (default encoding is 'ASCII'):
# UnicodeEncodeError: 'ascii' codec can't encode character u'\x80'
# in position 0: ordinal not in range(128)

if __name__ == '__main__':
    print('code pt 0x CP  URL encoding')
    for i in range(0x110000):
        print_unicode_entry(i)

# if you try this:
#    print(unicode_entry(0x110000))
# you'll get this:
# UnicodeDecodeError: 'unicodeescape' codec can't decode bytes in position 0-9: illegal Unicode character

# ValueError: unichr() arg not in range(0x10000) (narrow Python build)
# if we encode chars > 0x10000, this can be avoided

# read this: http://docs.python.org/howto/unicode.html
#
# unicode range is:
# 0-1,114,111 (0x10ffff in base-16).
# 1114111 - hi, I am a palindromic number
#
# http://docs.python.org/library/codecs.html#standard-encodings
#
# U-00000000 ... U-0000007F : 0xxxxxxx (this is ASCII, [7bits]
# U-00000080 ... U-000007FF : 110xxxxx 10xxxxxx
# U-00000800 ... U-0000FFFF : 1110xxxx 10xxxxxx 10xxxxxx
# U-00010000 ... U-0010FFFF : 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
