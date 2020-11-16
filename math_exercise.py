# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:29:59 2018

@author: nitingera
"""

import math
import random

side1=3
side2=4

hypotenuse = math.hypot(side1, side2)

print(hypotenuse)

deg1=180
rad1= 2
deg2 = 270
rad2 = 5

print(math.radians(180))
print(math.degrees(2))

x=0
sum = 0
while(x<100):
    number = random.randrange(1, 10)
    sum += number
    x += 1

print("sum = ", sum)
print("average =", sum/100)
