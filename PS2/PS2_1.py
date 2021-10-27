# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:11:47 2021

@author: ConanDoug
"""


import pandas as pd
Sig_Eqs = pd.read_csv('earthquakes-2021-10-25_21-55-55_+0800.tsv', sep='\t')

#1.1
Sig_Eqs_Deaths = Sig_Eqs.groupby('Country')['Deaths'].sum().sort_values(ascending=False)[0:10]
print(Sig_Eqs_Deaths)

#1.2
Sig_Eqs_Mag = Sig_Eqs
Sig_Eqs_Mag['Num'] = 1
Sig_Eqs_Mag_6 = Sig_Eqs[Sig_Eqs['Mag']>6.0].groupby('Year')['Num'].count()
axes = Sig_Eqs_Mag_6.plot(marker='.', linestyle='None', figsize=(11, 9), subplots=True)

#1.3
def CountEq_LargestEq(country):
    Sig_Eqs_Coun = Sig_Eqs
    Sig_Eqs_Coun['Num'] = 1
    sig_qus_country_num = Sig_Eqs_Coun.groupby('Country')['Num'].count()
    coun_num = sig_qus_country_num[country]
    coun = Sig_Eqs_Coun[Sig_Eqs_Coun['Country']==country]
    coun_max = coun['Mag'].max()
    if pd.isnull(coun_max):
        coun_max_line = coun
    else:
        coun_max_line = coun[coun['Mag']==coun_max]
    coun_y = coun_max_line.iloc[0,1].astype(int).astype(str)
    if pd.isnull(coun_max_line.iloc[0,2]):
        coun_max_line.iloc[0,2]=0.0
    coun_m = coun_max_line.iloc[0,2].astype(int).astype(str)
    if pd.isnull(coun_max_line.iloc[0,3]):
        coun_max_line.iloc[0,3]=0.0
    coun_d = coun_max_line.iloc[0,3].astype(int).astype(str)
    coun_date = coun_y+'/'+coun_m+'/'+coun_d
    return coun_num,coun_date

Sig_Eqs_Country = Sig_Eqs.groupby('Country')['Deaths'].sum()
Eqs_Num = []
for i in Sig_Eqs_Country.index:
    (a,b)=CountEq_LargestEq(i)
    Eqs_Num.append([i,a,b])
Sig_Eqs_Num=pd.DataFrame(Eqs_Num)
Sig_Eqs_Num.sort_values(1,ascending=False)
    