# Homework 5

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Forecasting one week
flow_in_Sep = (flow_data[(flow_data[:,0] >= 2010) & (flow_data[:,1]==9),3])
flow_quants = np.nanquantile(flow_in_Sep, q=[0, 0.25, 0.5, 0.75])
print('The flow quantiles in Sep after 2013:', flow_quants)
print('The maximum flow is', np.nanmax(flow_in_Sep))
print('The minium flow is', np.nanmin(flow_in_Sep))
print('The average flow in September after 2013 is', np.nanmean(flow_in_Sep))

print(np.nanmean(flow_data[(flow_data[:,0]==2023) & (flow_data[:,1]==9),3]))
# %%
# Forecasting two week
flow_in_Oct = (flow_data[(flow_data[:,0] >= 2010) & (flow_data[:,1]==10) & (flow_data[:,2] <=15),3])
flow_quants = np.nanquantile(flow_in_Oct, q=[0, 0.25, 0.5, 0.75])
print('The flow quantiles in Oct after 2010:', flow_quants)
print('The maximum flow is', np.nanmax(flow_in_Oct))
print('The minium flow is', np.nanmin(flow_in_Oct))
print('The average flow in October after 2010 is', np.nanmean(flow_in_Oct))
# %%
#Flow in September after 2010
flow_data1= (flow_data[(flow_data[:,0] >= 2010) & (flow_data[:,1] == 9),3])
mybins=np.linspace(0, 1000, num=20)
plt.hist(flow_data1, bins = mybins)
plt.title('Streamflow in September after 2010')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
# %%
# Flow in October since 2010 
mybins = np.linspace(0, 1000, num=20) 
plt.hist(flow_in_Oct, bins = mybins)
plt.title('Streamflow before 15th in October since 2010')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
# %%
# Assignment
flow_5yr = flow_data[(flow_data[:,0] >= 2015) & (flow_data[:,0] <= 2019),:] 
print(flow_5yr)
print('The dimension of flow_5yr is', np.ndim(flow_5yr))
print('The average flow of the five years is', np.mean(flow_5yr[:,3]), 'cfs')
print(flow_5yr.shape)
print(type(flow_5yr))
# %%
# For loop
flow_5yr1=np.zeros(((365*5+1),4))
j=0
for i in range(len(flow_data[:,0])):
       if flow_data[i,0] >= 2015 and flow_data[i,0] <= 2019:
             flow_5yr1[j,:]=(flow_data[i,:])
             j=j+1
print(flow_5yr1)
print(type(flow_5yr1))
print(np.ndim(flow_5yr1))
print(np.mean(flow_5yr1))
# %%
# Flow_daily
# method 1 without for loop
flow_daily=np.array(flow_5yr)
flow_daily[:,3] *= 86400
print(flow_daily[0:5,3])
print('The entire time period is', np.sum(flow_daily[:,3]), 'cubic feet')
# %%
# method 2 for loop
for i in range(len(flow_5yr[:,3])):
    flow_5yr[i:3] *= 86400
    flow_daily = flow_5yr
print(flow_daily[0:5,3])      
     
# %%
# Flow_monthly
#Build the year and month column
flow_monthly = np.zeros((60,3))
flow_monthly[:,0] = np.repeat(np.arange(2015, 2020, 1), 12)
flow_monthly[:,1] = np.tile(np.arange(1,13,1),5)
print(flow_monthly)
# %%
for i in range(60):
     year = flow_monthly[i,0]
     month = flow_monthly[i,1]
     #print(year, month)
     ilist = (flow_5yr[:,0] == year) & (flow_5yr[:,1] == int(month))
     flow_monthly[i,2]= np.nanmean(flow_5yr[ilist,3])
     print(year, month, flow_monthly[i,2])

print(flow_monthly[0:5,:])

