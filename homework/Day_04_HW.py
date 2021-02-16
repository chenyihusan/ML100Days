
# coding: utf-8

# In[1]:

import numpy as np
#1.有多少學生英文成績比數學成績高?
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
Ebetter=np.greater(english_score,math_score)
Ebetter


# In[2]:

#2.是否全班同學最高分都是國文?
Cbest=np.greater(chinese_score,english_score)
Cbest


# In[ ]:



