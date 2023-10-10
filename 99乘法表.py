# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 22:31:38 2023

@author: Nitro
"""

for i in range (1, 10):
    for j in range (1,10):
        product = i * j
        print("%d * %d = %2d " % (i,j,product), end = "")
    print()