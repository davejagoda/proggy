#!/usr/bin/env python3

import time
reward = 50
sum = 0
print('               %BTC mined                                 reward')
print('{:40.36f} {:40.36f}'.format(sum, reward))
while True:
    time.sleep(0.5)
    sum += reward
    reward = reward / 2.0
    print('{:40.36f} {:40.36f}'.format(sum, reward))
    if sum >= 100:
        print('sum >= 100')
        break
    if reward <= 0:
        print('reward <= 0')
        break
