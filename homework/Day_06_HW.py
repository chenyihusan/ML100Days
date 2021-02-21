
# coding: utf-8

# In[2]:

import numpy as np
#1. 將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])
array3 = np.array([2,4,6])


# In[3]:

with open('one_array.npz', 'wb') as f:
    np.save('one_array.npz',array1,array2) 


# In[4]:

npzfile['array1'] 


# In[5]:

with open('one_array.npz', 'wb') as f:
    np.savez('one_array.npz',a=array1,b=array2) 


# In[6]:

myArch = np.load('one_array.npz')
myArch['b']


# In[7]:

with open('one_array.npz', 'wb') as f:
    np.savez('one_array.npz',a=array1,b=array2,c=array3) 


# In[8]:

myArch = np.load('one_array.npz')
myArch['c']


# In[9]:

#2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔
myArch = np.load('one_array.npz')
myArch['c']


# In[ ]:



