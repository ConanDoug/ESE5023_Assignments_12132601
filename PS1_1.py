# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:36:50 2021

@author: ConanDoug
"""

def Print_values(a,b,c):
    if a > b:
        if b > c:
            print(a,b,c)
        else:
            if a > c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b > c:
            '''
            if a > c:
                print(b,a,c)
            else:
                print(b,c,a)
                '''
        else:
            print(c,b,a)
    return