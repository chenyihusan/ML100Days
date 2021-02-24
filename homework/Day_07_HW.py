
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

#1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
array1 = np.array([[10, 8], [3, 5]])
aa=np.linalg.inv(array1)
aa  #反矩陣


# In[3]:

bb=array1*aa
bb


# In[4]:

#2. 運用上列array計算特徵值、特徵向量?
# eigenvalues
array1 = np.array([[10, 8], [3, 5]])
w, v = np.linalg.eig(array1)
print(w)
print(v)


# In[5]:

#3. 運用上列array計算SVD?
u, s, vh = np.linalg.svd(array1)
print(u)
print(s)
print(vh)


# In[ ]:



