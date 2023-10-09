# Starter code for week 6 Pandas

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Warm up exercises: 

# %%
# 1. How do you see a quick summary of what is in `data`?
print(data.info())
print(data.describe())
# %%
# 2. How do you get a listing of the columns in `data`?
data.iloc[0,:]
# %%
# 3. How do you select the streamflow column in `data`?
data['flow']
#%%
# 5. How do you get the last streamflow value from `data`?
print(data.iloc[[-1]])

#%%
# 6. What is the mean streamflow value for entire period?
print(data['flow'].mean())
#%%
# 7. What is the maximum value for the entire period?
print(data['flow'].max())
#%%
# 8. How do you find the maximum streamflow value for each year?
yearly_sum = data.groupby('year').agg('max')
print(yearly_sum)
# %%
# assignment 3
monthly_sum = data.groupby('month')
print(monthly_sum['flow'].describe())
# %%
# assignment 4
lowest=data.sort_values(by = "flow").head()
highest=data.sort_values(by = "flow").tail()
summary1 =pd.DataFrame(lowest, columns=['datetime','month','flow'])
summary2 =pd.DataFrame(highest, columns=['datetime','month','flow'])
summary= pd.concat([summary2, summary1])
print(summary)
# %%
#assignment 5
cateria = data.loc[(data['flow'] <= 94.171) & (data['flow'] >= 77.049)]

print(cateria)
# %%
# forecast one week
Oct_data1 = data.loc[(data['year'] >= 2010) & (data['month'] == 10) & (data['day'] <= 15)]
pick_data1=Oct_data1.groupby('year').agg({'flow':['mean','min','max']})
print('The describe of the flow data in Oct after 2010' )
print(Oct_data1.describe())
print('This the info of pick data')
print(pick_data1)
print('One week forecast is', pick_data1.iloc[-5:-3,0].mean())
# %%
# forecast two week
Oct_data2 = data.loc[(data['year'] >= 2010) & (data['month'] == 10) & (data['day'] >= 15)]
pick_data2=Oct_data2.groupby('year').agg({'flow':['mean','min','max']})
print('The describe of the flow data in Oct after 2010' )
print(Oct_data2.describe())
print('This the info of pick data')
print(pick_data2)
print('Two week forecast is', pick_data2.iloc[-4:-2,0].mean())
# %%
