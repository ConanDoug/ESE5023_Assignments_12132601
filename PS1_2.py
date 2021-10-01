# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:50:12 2021

@author: ConanDoug
"""

import numpy as np
 
M1 = np.random.randint(0,50,(5,10))
M2 = np.random.randint(0,50,(10,5))

def Matrix_multip(A,B):
    m=np.zeros([5,5],dtype=int) 
    for i in range(5):
        for j in range(5):
            for k in range(10):
                m[i,j]+= M1[i,k] * M2[k,j]
    return m

Matrix_multip(M1,M2)