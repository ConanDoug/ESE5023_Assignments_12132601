# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:28:25 2021

@author: ConanDoug
"""

def Pascal_triangle(k):
    x = []
    for i in range(k):
        if i == 0:
            x.append([1])
        elif i == 1:
            x.append([1,1])
        else:
            y = []
            for j in range(i+1):
                if j == 0 or j == i:
                    y.append(1)
                else:
                    y.append(x[i-1][j-1]+x[i-1][j])
            x.append(y)
    return x[k-1]