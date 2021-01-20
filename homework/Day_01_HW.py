#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
a=np.arange(0,20,1)


# In[4]:


print(a)


# In[5]:


#2.呈上題，將以上數列取出偶數。
print(a[0:18:2])


# In[6]:


#3.呈1題，將數列取出3的倍數。
print(a[0:19:3])


# In[ ]:




