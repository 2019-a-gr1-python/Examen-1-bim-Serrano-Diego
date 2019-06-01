# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:41:17 2019

@author: jukis
"""

import pandas as pd
import numpy as np
###11
### lista
mylist = list('abcedfghijklmnopqrstuvwxyz')
data = mylist
s_list= pd.Series(data)
print(s_list)
###array
myarr = np.arange(26)
data = myarr
s_array = pd.Series(data)
print (s_array)
### diccionario
mydict = dict(zip(mylist, myarr))
data = mydict
s_dic = pd.Series(data)
print (s_dic)

### 12

a= pd.DataFrame({'indice':s_dic.index, 'valor':s_dic.values,})
print (a)


### 13
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
a = pd.concat([ser1, ser2], axis=1).reset_index()
print (a)
###14
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

df = pd.DataFrame({"1":ser1, "ser2":ser2})


###15

### 16
serie = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

serie.value_counts()
### 17

###18

### 19
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
df2 = pd.DataFrame({"a":[1, 2, 3], 
                    "b":[5, 6, 7]}) 
df.append(ser1, ignore_index = True) 
df.append(ser2, ignore_index = True) 