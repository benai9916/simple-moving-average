#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In[39]:
import quandl
from matplotlib import style
style.use("fivethirtyeight")

# In[10]:


api_key = 'Hwo7VYQAWrbmNxRxBVi2'


# In[70]:

data = quandl.get('NSE/PNB', trim_start='2017-08-01', trim_end='2018-04-30', api_key=api_key)


# In[27]:

# In[91]:


data['15d'] = np.round(data['Close'].rolling(window=30).mean(), 2)
data['40d'] = np.round(data['Close'].rolling(window=40).mean(), 2)
# data[['Close', '15d', '40d']].plot(grid=True, figsize=(10,5))
data['15d - 40d'] = data['15d']- data['40d']
x=40
data['Stance'] = np.where(data['15d - 40d']>x,1,0)
data['Stance'] = np.where(data['15d - 40d']<x,-1,data['Stance'])
data['Stance'].value_counts()

data['Stock_Returns'] = np.log(data['Close'] / data['Close'].shift(1))
data['SMA_Strategy'] = data['Stock_Returns'] * data['Stance'].shift(1)
data[['Stock_Returns', 'SMA_Strategy']].plot(grid=True, figsize=(12,6))
plt.show()

# In[ ]:




