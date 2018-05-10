#!/usr/bin/env python3

import sys

scale = ['C', 'C#', 'D', 'D#', 'E',
         'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
majorChords = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
minorChords = [chord.lower() for chord in majorChords]
intervals = [0, 2, 4, 5, 7, 9, 11]

#print(len(scale), scale)
#print(len(majorChords), majorChords)
#print(len(minorChords), minorChords)
#print(len(intervals), intervals)

for arg in sys.argv[1:]:
    if arg not in majorChords and arg not in minorChords:
        print('invalid argument')
        sys.exit(1)

output = ''
for root in scale:
    for arg in sys.argv[1:]:
        if arg in majorChords:
            i = (intervals[majorChords.index(arg)] + scale.index(root)) % len(scale)
            output = output + scale[i] + '  '
        else:
            i = (intervals[minorChords.index(arg)] + scale.index(root)) % len(scale)
            output = output + scale[i] + 'm '
        if 0 != len(output) % 4:
            output = output + ' '
    print(output)
    output = ''
