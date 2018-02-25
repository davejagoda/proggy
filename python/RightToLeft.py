#!/usr/bin/python

rtl = chr(0x202e).encode('utf8')
ltr = chr(0x202d).encode('utf8')
pop = chr(0x202c).encode('utf8')

print(('hi', rtl, 'hi', ltr, 'hi'))
print(('hi', rtl, 'hi', pop, 'hi'))

