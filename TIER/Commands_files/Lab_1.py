#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd


# In[52]:


data = pd.read_excel('/Users/pawelkocwa/Documents/STUDIA/SEMESTR_7/AiBD/Lab1/TIER_Documetnation_TB/Anal/dem_score.xlsx')


# In[53]:


data.head()


# In[54]:


data_melt = pd.melt(data, id_vars=["country"])


# In[58]:


data_melt.head()


# In[61]:


data_rename = data_melt.rename(columns={"variable":"year", "value":"lvl_of_democracy"})#df.rename(columns={"A": "a", "B": "c"})


# In[62]:


data_rename.head()


# In[64]:


data_rename.to_csv('/Users/pawelkocwa/Documents/STUDIA/SEMESTR_7/AiBD/Lab1/TIER_Documetnation_TB/Analysis_data/dem_score_.csv')


# In[ ]:




