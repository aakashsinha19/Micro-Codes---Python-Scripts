# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:06:19 2018

@author: as19153
"""

import time
print("Timer to calculate actual Office hours")

start = input("Would you like to begin Timing? (y/n): ")
if start == "y":
    timeLoop = True

Sec = 0
Min = 0
Hour = 0

timeLoop = start
while timeLoop:
    Sec += 1
    print(str(Hour) + " Hour " + str(Min) + " Mins " + str(Sec) + " Sec ")
    time.sleep(1)
    if Sec == 60:
        Sec = 0
        Min += 1
        print(str(Hour) + " Hour " + str(Min) + " Minutes ")
        if Min == 60:
            Sec = 0
            Min = 0
            Hour += 1
