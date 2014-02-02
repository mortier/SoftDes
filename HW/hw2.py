# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/dmichael/.spyder2/.temp.py
"""

from math import *
r=5
volume = 4.0/3.0 * pi*r**2
print  volume

cost = 24.95*.6*60+3+59*.75
print  cost

slow = (8*60+15)
fast = (7*60+12)
start = 6*60*60+52*60
runtime = 2*slow+3*fast
end = runtime + start
sec = end % 60
minu = (end / 60) % 60
hour = end/60/60
print str(hour) + ":" + str(minu) + ":" + str(sec)
