
# coding: utf-8

# Author: Dr. Jack K. Rasmus-Vorrath

# # Question 1: Creating a float list

# In[6]:

x = [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]


# Q 1a: Printing the 5th element

# In[7]:

print(x[4])


# Q 1b: Appending to the list

# In[8]:

x.append(55.2)


# In[9]:

x


# Q 1c: Removing (and returning) the 6th element

# In[10]:

x.pop(5)


# In[11]:

x


# Q 1d: Iteratively printing values greater than 45

# In[12]:

for i in x:			
    if i > 45:
        print(i)


# # Question 2: Numpy Arrays and Summary Statistics

# Q 2a: Library import

# In[13]:

import numpy as np


# Q 2b: Creating an array

# In[14]:

y = np.array([45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6])


# Q 2c: Summary statistics

# In[16]:

np.mean(y)


# In[17]:

np.std(y)


# Q 2d: Logical referencing, retrieving values less than 45

# In[21]:

print(y[np.where( y<45 )])


# Q 2e: Maximum and minimum values

# In[22]:

np.max(y)


# In[26]:

np.min(y)


# # Question 3: Dataframes in Pandas and Seaborn

# Q 3a: Library Import

# In[44]:

import pandas as pd


# Q 3b: Reading in the dataframe (adjusting filepath)

# In[29]:

iris = pd.read_csv('C:/Users/jkras/Desktop/Iris.csv')


# Q 3c: Displaying dataframe head

# In[30]:

iris.head()


# Q 3d: Dropping 'Id' column

# In[31]:

df = pd.DataFrame(iris)

df.drop('Id', axis=1)


# Q 3e: Subsetting by 'Setosa' species

# In[32]:

z = df.loc[df['Species'] == 'Iris-setosa']


# In[34]:

print(z)


# Q 3f: Summary statistics on dataframe for species 'Setosa'

# In[36]:

sub_df = pd.DataFrame(z)


# In[38]:

sub_df.describe()


# Q 3g: Summary statistics on dataframes grouped by 'Species'

# In[72]:

w = df.drop('Id', axis=1)

s = w.groupby('Species')

s.describe()


# Q 3h: Creating boxplots by 'Species'

# In[74]:

import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')

s.boxplot(layout = (1,3), figsize = (20,8))


# Q 3i: Seaborn scatterplot matrix by 'Species'

# In[75]:

import seaborn as sns

sns.pairplot(iris, hue = 'Species')


# In[ ]:



