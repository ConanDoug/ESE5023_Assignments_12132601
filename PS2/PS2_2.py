# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:51:43 2021

@author: ConanDoug
"""

import pandas as pd
import time
WS_SZ = pd.read_csv('2281305.csv', low_memory=False)


date_1 = []
for i in WS_SZ.iloc[:,1:2].values.tolist(): 
    dt = time.strptime(i[0], "%Y-%m-%dT%H:%M:%S")
    date_1.append(str(dt.tm_year)+'-'+str(dt.tm_mon))
WS_SZ['DATE']=date_1

temp = []
for data in WS_SZ.iloc[:,42:43].values.tolist():
    temp1 = data[0].split(',')
    temp.append(int(temp1[3]))

WS_SZ['wind_sp']=temp
WS_SZ['DATE'] = pd.to_datetime(WS_SZ['DATE'])
WS_SZ = WS_SZ.set_index('DATE')
WS_SZ_plot = WS_SZ.groupby('DATE')['wind_sp'].mean()
WS_SZ_plot.plot()