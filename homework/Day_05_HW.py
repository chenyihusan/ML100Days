
# coding: utf-8

# In[1]:

import numpy as np
#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])
maxscore1=np.average(english_score)
print(maxscore1)
maxscore2=np.average(math_score)
print(maxscore2)
maxscore3=np.average(chinese_score)
print(maxscore3)


# In[2]:

maxscore1=np.max(english_score)
print(maxscore1)
maxscore2=np.max(math_score)
print(maxscore2)
maxscore3=np.max(chinese_score)
print(maxscore3)


# In[3]:

maxscore1=np.min(english_score)
print(maxscore1)
maxscore2=np.min(math_score)
print(maxscore2)
maxscore3=np.min(chinese_score)
print(maxscore3)


# In[4]:

maxscore1=np.std(english_score)
print(maxscore1)
maxscore2=np.std(math_score)
print(maxscore2)
maxscore3=np.std(chinese_score)
print(maxscore3)


# In[5]:

#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
maxscore1=np.average(english_score)
print(maxscore1)
maxscore2=np.average(math_score)
print(maxscore2)
maxscore3=np.average(chinese_score)
print(maxscore3)


# In[6]:

maxscore1=np.max(english_score)
print(maxscore1)
maxscore2=np.max(math_score)
print(maxscore2)
maxscore3=np.max(chinese_score)
print(maxscore3)


# In[7]:

maxscore1=np.min(english_score)
print(maxscore1)
maxscore2=np.min(math_score)
print(maxscore2)
maxscore3=np.min(chinese_score)
print(maxscore3)


# In[8]:

maxscore1=np.std(english_score)
print(maxscore1)
maxscore2=np.std(math_score)
print(maxscore2)
maxscore3=np.std(chinese_score)
print(maxscore3)


# In[9]:

#3. 用補考後資料找出與國文成績相關係數最高的學科?corrcoef
maxscore1=np.corrcoef(english_score)
print(maxscore1)
maxscore2=np.corrcoef(math_score)
print(maxscore2)
maxscore3=np.corrcoef(chinese_score)
print(maxscore3)


# In[10]:

#3. 用補考後資料找出與國文成績相關係數最高的學科?corrcoef
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
corrscore1=np.corrcoef(english_score)
print(corrscore1)
corrscore2=np.corrcoef(math_score)
print(corrscore2)
corrscore3=np.corrcoef(chinese_score)
print(corrscore3)


# In[11]:

#3. 用補考後資料找出與國文成績相關係數最高的學科?corrcoef
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
corrscore1=np.corrcoef(english_score)
print(corrscore1)
corrscore2=np.corrcoef(math_score)
print(corrscore2)
corrscore3=np.corrcoef(chinese_score)
print(corrscore3)


# In[12]:

#3. 用補考後資料找出與國文成績相關係數最高的學科?corrcoef
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
corrscore1=np.corrcoef(chinese_score,english_score)
print(corrscore1)
corrscore2=np.corrcoef(chinese_score,math_score)
print(corrscore2)
corrscore3=np.corrcoef(chinese_score,chinese_score)
print(corrscore3)


# In[ ]:



