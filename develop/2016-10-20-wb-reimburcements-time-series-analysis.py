
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# In[2]:

previous_years_data = pd.read_csv('../data/2016-08-08-previous-years.xz',
                   usecols = ['month', 'year', 'congressperson_id', 'net_value'],
                   dtype={'congressperson_id': np.str,
                          'month': np.str,
                          'year': np.str})

last_year_data = pd.read_csv('../data/2016-08-08-last-year.xz',
                   usecols = ['month', 'year', 'congressperson_id', 'net_value'],
                   dtype={'congressperson_id': np.str,
                          'month': np.str,
                          'year': np.str})

#Concatenating the datasets
data = pd.concat([last_year_data, previous_years_data])

#Joining month and year columns into a datetime field
data['month'] = pd.to_datetime(data['month']+'-'+data['year'], format='%m-%Y')

#Year field is now unnecessary
data.drop('year', 1, inplace=True)
data.head()


# In[3]:

aggregate = {
    'congressperson_id': {
       'total': 'nunique'   
    },
    'net_value': {
        'mean': 'mean'
    }
}

monthly_group = data.groupby('month').agg(aggregate)
monthly_group.head()


# In[4]:

figsize = (8*(len(monthly_group.index)/48), 2.5*len(monthly_group.columns))
monthly_group.plot(figsize=figsize, color=['r', 'b', 'g'], grid='on', subplots=True)


# ### Questions
# 
# - Why the period before 2011 looks messy?
# - From 2011 onwards a pattern appears. What is responsible for the raise in the mean at the end o each year?
# - Why the mean gets higher at the end of 2014? Is it a reflex of the elections?
# - Why the number of deputys getting reimburcements go up at the begining of 2011? Is it a kind of hype? There were changes in the law at that time?

# In[ ]:



