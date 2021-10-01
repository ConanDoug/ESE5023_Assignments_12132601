# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:58:58 2021

@author: ConanDoug
"""
import matplotlib.pyplot as plt

def Find_expression(x):
    a = ['','+','-']
    m = 0
    for i0 in range(3):
        for i1 in range(3):
             for i2 in range(3):
                  for i3 in range(3):
                       for i4 in range(3):
                            for i5 in range(3):
                                 for i6 in range(3):
                                      for i7 in range(3):
                                          n = '1'+a[i0]+'2'+a[i1]+'3'+a[i2]+'4'+a[i3]+'5'+a[i4]+'6'+a[i5]+'7'+a[i6]+'8'+a[i7]+'9'
                                          #m.append(eval(n))
                                          if eval(n) == x:
                                              print(n, '=', x)
                                              m+=1
    return m

Total_solutions = [0]*100
for i in range(1,101):
    Total_solutions[i-1]=Find_expression(i)
num = range(1,101)
plt.plot(num, Total_solutions)
plt.show()

Total_solutions_max = max(Total_solutions)
Total_solutions_min = min(Total_solutions)
for i in range(100):
    if Total_solutions[i] == Total_solutions_max:
        print(i,'yields the maximum of Total_solutions')
    elif Total_solutions[i] == Total_solutions_min:
        print(i,'yields the minimum of Total_solutions')
         