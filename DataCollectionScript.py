#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

columns = ['Kind','Name','CountLineCode','CountClassBase', 'CountClassCoupled',
       'CountClassDerived', 'CountDeclMethodAll', 'CountDeclMethod',
       'MaxInheritanceTree', 'PercentLackOfCohesion',
       'CountDeclInstanceMethod', 'CountDeclInstanceVariable']

metrics = ['CountLineCode','CountClassBase', 'CountClassCoupled',
       'CountClassDerived', 'CountDeclMethodAll', 'CountDeclMethod',
       'MaxInheritanceTree', 'PercentLackOfCohesion',
       'CountDeclInstanceMethod', 'CountDeclInstanceVariable']

# def f(s) :
#     if s==True :
#         return 'Yes'
#     else :
#         return 'No'

def func(version1,version2) :
    csv1 = pd.read_csv(version1)
    csv1 = csv1[columns]
    csv1.dropna(inplace=True)
    csv1 = csv1[csv1.CountLineCode > 0]
    
    csv2 = pd.read_csv(version2)
    csv2 = csv2[columns]
    csv2.dropna(inplace=True)
    csv2 = csv2[csv2.CountLineCode > 0]
    
    names = csv1.Name.tolist()
    ans = []
    for i in names :
        v2 = csv2[csv2.Name == i]
        if not v2.empty :
            v1 = csv1[csv1.Name == i]
            x = True
            for j in metrics :
                x = x and (v1.iloc[0][j] == v2.iloc[0][j])
            if x == False :
                if v1.iloc[0]['CountLineCode'] == v2.iloc[0]['CountLineCode'] :
                    ans.append('Modified')
                elif v1.iloc[0]['CountLineCode'] > v2.iloc[0]['CountLineCode'] :
                    ans.append('Lines Decreased')
                else :
                    ans.append('Lines Increased')
            else :
                ans.append('No Change')
        else :
            ans.append('Class Deleted')
    csv1['Change'] = ans
#     csv1["Change in class"] = csv1.Change.apply(f)
#     del csv1["Change"]
    csv1.to_csv('Timber-0.2b1Change.csv') #Change the name of saving file
    

ver1 = 'Timber-0.2b.csv' #Change the name of version 1
ver2 = 'Timber-0.3b.csv' #Change the name of version 2

func(ver1,ver2)


# In[52]:




