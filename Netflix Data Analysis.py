#!/usr/bin/env python
# coding: utf-8

# In[21]:


# importing lib.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[22]:


# loading dataset
df = pd.read_csv('mymoviedb.csv', lineterminator='\n')
df.head()


# In[23]:


# viewing dataset info
df.info()


# In[24]:


# exploring genres column
df['Genre'].head()


# In[25]:


# check for duplicated rows
df.duplicated().sum()


# In[26]:


# exploring summary statistics
df.describe()


# In[27]:


# Casting Release_Date column and extracting year values
df['Release_Date'] = pd.to_datetime(df['Release_Date'])

# confirming changes
print(df['Release_Date'].dtypes)


# In[28]:


df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes


# In[29]:


df.info()


# In[30]:


df.head()


# In[31]:


df.head()


# In[32]:


# making list of column to be dropped
cols = ['Overview', 'Original_Language', 'Poster_Url']


# In[33]:


# dropping columns and confirming changes
df.drop(cols, axis=1, inplace=True)
df.columns


# In[34]:


df.head()


# In[35]:


# categorizing Vote_Average column
def catigorize_col (df, col, labels):
    """
    catigorizes a certain column based on its quartiles
    
    Args:
    (df) df - dataframe we are proccesing
    (col) str - to be catigorized column's name 
    (labels) list - list of labels from min to max
    
    Returns:
    (df) df - dataframe with the categorized col
    """
    
    # setting the edges to cut the column accordingly
    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]
             
    df[col] = pd.cut(df[col], edges, labels=labels, duplicates='drop')
    return df


# In[36]:


# define labels for edges
labels = ['not_popular', 'below_avg', 'average', 'popular']

# categorize column based on labels and edges
catigorize_col(df, 'Vote_Average', labels)

# confirming changes
df['Vote_Average'].unique()


# In[37]:


df.head()


# In[38]:


# exploring column
df['Vote_Average'].value_counts()


# In[39]:


# dropping NaNs
df.dropna(inplace=True)

# confirming
df.isna().sum()


# In[40]:


df.head()


# In[41]:


# split the strings into lists
df['Genre'] = df['Genre'].str.split(', ')

# explode the lists
df = df.explode('Genre').reset_index(drop=True)
df.head()


# In[42]:


# casting column into category
df['Genre'] = df['Genre'].astype('category')

# confirming changes
df['Genre'].dtypes


# In[43]:


df.info()


# In[44]:


df.nunique()


# In[45]:


# setting up seaborn configurations
sns.set_style('whitegrid')


# In[46]:


# showing stats. on genre column
df['Genre'].describe()


# In[47]:


# visualizing genre column
sns.catplot(y='Genre', data=df, kind='count',
            order=df['Genre'].value_counts().index,
            color='#4287f5')
plt.title('genre column distribution')
plt.show()


# In[48]:


# visualizing vote_average column
sns.catplot(y='Vote_Average', data=df, kind='count',
            order=df['Vote_Average'].value_counts().index,
            color='#4287f5')
plt.title('votes destribution')
plt.show()


# In[49]:


# checking max popularity in dataset
df[df['Popularity'] == df['Popularity'].max()]


# In[50]:


# checking min popularity in dataset
df[df['Popularity'] == df['Popularity'].min()]


# In[51]:


df['Release_Date'].hist()
plt.title('Release_Date column distribution')
plt.show()


# In[ ]:




