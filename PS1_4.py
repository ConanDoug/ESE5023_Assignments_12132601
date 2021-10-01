# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:51:15 2021

@author: ConanDoug
"""

import numpy as np
 
y = np.random.randint(1,101)
def Least_moves(x):
    m = x
    n = 0
    while x > 1:
        if x % 2:
            x = (x-1) / 2
            n += 2
        else:
            x /= 2
            n += 1
    print(" The smallest number of moves you have to make to get to exactly",m, "RMB is", n)     
    return 
Least_moves(y)