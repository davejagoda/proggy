#!/usr/bin/env python3

# bibliography: http://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user

import sys
import termios
import tty

fd = sys.stdin.fileno()
save = termios.tcgetattr(fd)
tty.setraw(fd)
c = sys.stdin.read(1)
termios.tcsetattr(fd, termios.TCSADRAIN, save)
print(c)
