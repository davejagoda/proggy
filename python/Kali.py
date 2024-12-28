#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unicodedata

kali = chr(0x0915) + chr(0x093E) + chr(0x0932) + chr(0x0940)

print(unicodedata.normalize("NFC", kali))

# U+0915 क &#2325;
# DEVANAGARI LETTER KA
# U+093e ा &#2366;
# DEVANAGARI VOWEL SIGN AA
# U+0932 ल &#2354;
# DEVANAGARI LETTER LA
# U+0940 ी &#2368;
# DEVANAGARI VOWEL SIGN II
