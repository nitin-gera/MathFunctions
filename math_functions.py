# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:18:36 2018

@author: nitingera
"""

import math
import random

value1 = 100
value2 = 250.5

print(int(value2))
print(float(value1))

diff = value1 - value2

print(diff)
absolute_diff = abs(diff)
print(absolute_diff)

print(math.ceil(diff))
print(math.floor(diff))
print(pow(3,4))

x = 0
while(x < 10):
    print(random.randrange(1, 100))
    x += 1

dt_group=["Deepika", "Kranti", "Rupesh", "Nitin", "Devesh", "Neha", "Anu"]

print(random.choice(dt_group))

random.shuffle(dt_group)

print(dt_group)

