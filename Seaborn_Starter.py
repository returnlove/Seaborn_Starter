
# coding: utf-8

# In[4]:


get_ipython().magic('matplotlib inline')
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[ ]:


# Article reference
# https://elitedatascience.com/python-seaborn-tutorial


# In[2]:


df = pd.read_csv('Pokemon.csv', encoding = "utf-8")


# In[3]:


df.head()


# In[10]:


# Scatterplot arguments
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, # No regression line
           hue='Stage')   # Color by evolution stage


# In[11]:


# Scatterplot arguments
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, # No regression line
           hue='Stage')   # Color by evolution stage

# customize seaborn using matplotlib. Searborn is highlevel package of matplotlib
plt.ylim(0,200)
plt.xlim(0,200)

