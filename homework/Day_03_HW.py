#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 


# In[2]:


#1.正常的談話的聲壓為20000微巴斯卡，請問多少分貝?
#請寫下程式
V1 = 20000
V0 = 20
G=20*np.log10(V1/V0)
G


# In[4]:


#2. 30分貝的聲壓會是50分貝的幾倍?
#公式移項過後可以得到 V1 = ?
#請寫下程式V0=20
GB2=50
GB=30
V30=10**(GB/V0)*20
V50=10**(GB2/V0)*20
ans=V50/V30
print(V30)
print(V50)
print(ans)


# In[ ]:




