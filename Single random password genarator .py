#!/usr/bin/env python
# coding: utf-8

# In[29]:


import random

l = "abcdefghijklmnopqrstuvwxyz"
u = l.upper()
n = "0123456789"
s = "+=-_?/!@#$"

all = l+u+n+s
len = 6
passw = "".join(random.sample(all,len))
print("Your Random Generated password is : "+passw)

