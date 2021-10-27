# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:43:12 2021

@author: ConanDoug
"""

import pandas as pd
import time
#3.1
precip = pd.read_csv('419220-99999-2019.csv')
precip.fillna(0)
#3.2    
precip['YEARMODA']=precip['YEARMODA'].astype(str)
date_1=[]
for i in precip.iloc[:,4:5].values.tolist(): 
    dt = time.strptime(i[0], "%Y%m%d")
    date_1.append(str(dt.tm_year)+'-'+str(dt.tm_mon)+'-'+str(dt.tm_mday))
precip['DATE']=date_1
   
precip['DATE'] = pd.to_datetime(precip['DATE'])
precip = precip.set_index('DATE')
precip['TEMP'].plot()
#3.3
print("The maximum of the temperature is",precip['TEMP'].max())
print("The minimum of the temperature is",precip['TEMP'].min())
print("The mean of the temperature is",precip['TEMP'].mean())
print("The median of the temperature is",precip['TEMP'].median())
print("The standard deviation of the temperature is",precip['TEMP'].std())
