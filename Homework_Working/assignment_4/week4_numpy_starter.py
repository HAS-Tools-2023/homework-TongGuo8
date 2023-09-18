# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('homework/Homework-TongGuo8/data', filename)
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
# Starter Code
# Count the number of values with flow > 600 and month ==7
flow_count = np.sum((flow_data[:,3] > 105.97) & (flow_data[:,1]==9))

criteria = (flow_data[:, 3] > 105.97) & (flow_data[:, 1] == 9)
pick_data = flow_data[criteria, 3]
flow_mean = np.mean(pick_data)

# Calculate the average flow for these same criteria 

flow_mean = np.mean(flow_data[(flow_data[:,3] > 105.97) & (flow_data[:,1]==9)])

print("Flow meets this critera", flow_count, " times in September")
print('And has an average value of', flow_mean, "when this is true")

# Question 4
flow_count1 = np.sum((flow_data[:,3] > 105.97) & (flow_data[:,0] <= 2000) & (flow_data[:,1]==9))
criteria = (flow_data[:, 3] > 105.97) & (flow_data[:, 1] == 9) & (flow_data[:,0] <= 2000)
pick_data = flow_data[criteria, 3]
flow_mean = np.mean(pick_data)
flow_count2 = np.sum((flow_data[:,0] <= 2000) & (flow_data[:,1] == 9))
print("Flow meets this critera", flow_count1, " times in September before 2000")
print("The percentage of the critera is", flow_count1 / flow_count2)

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.nanquantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.nanquantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2[:,3])

# %%
# my code
flow_in_Sep = (flow_data[(flow_data[:,0] >= 2010) & (flow_data[:,2] >= 17) & (flow_data[:,2] <= 23) & (flow_data[:,1]==9),3])
print(np.mean(flow_in_Sep), np.std(flow_in_Sep))
flow_array = np.array([[74.41, 3.81],
                      [136.34, 28.28],
                      [92.66, 14.93],
                      [213, 46.16], 
                      [175.86, 20.62],
                       [105.97, 25.14],
                       [98.79, 23.76],
                       [89.46, 5.28],
                       [141, 11.25],
                       [58.31, 4.05],
                       [59.3, 3.91],
                       [84.32, 12.48], 
                       [134, 27.74]])
print(flow_array[:,0])
flow_in_Sep2 = (flow_data[(flow_data[:,0] >= 2010) & (flow_data[:,1]==9),3])
print(np.max(flow_in_Sep2), np.min(flow_in_Sep2))
flow_in_Sep3 = (flow_data[(flow_data[:,0] <= 2000) & (flow_data[:,1]== 9),3])
print(np.max(flow_in_Sep3), np.min(flow_in_Sep3))
# %%
# The quantlies of flow in September 17th- 23rd after 2010
flow_quants1 = np.nanquantile(flow_in_Sep, q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# %%
# The quantlies of flow in September after 2010
flow_quants2 = np.nanquantile(flow_in_Sep2, q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants2)
# %%
# The quantlies of flow in September before 2000
flow_quants3 = np.nanquantile(flow_in_Sep3, q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants3)
# %%
flow_Sep_2023 = np.array(flow_data[(flow_data[:,0] == 2023) & (flow_data[:,1]==9),3])
print(np.mean(flow_Sep_2023), np.std(flow_Sep_2023))
flow_quants_23 = np.nanquantile(flow_Sep_2023, q=[0, 0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants_23)
# %%
# The flow in September 17th - 23rd after 2010 
mybins = np.linspace(0, 500, num=15) 
plt.hist(flow_in_Sep, bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
# %%
# The flow in September after 2010
mybins = np.linspace(0, 500, num=10) 
plt.hist(flow_in_Sep2, bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
# %%
# The flow in September before 2000
mybins = np.linspace(64, 1000, num=15) 
plt.hist(flow_in_Sep3, bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
# %%
print(flow_data.dtype)
print(flow_data.ndim, flow_data.size)
# %%
flow_count1 = np.sum((flow_data[:,3] > 105.97) & (flow_data[:,1]==9))
criteria = (flow_data[:, 3] > 105.97) & (flow_data[:, 1] == 9) 
pick_data = flow_data[criteria, 3]
flow_mean = np.mean(pick_data)
flow_count2 = np.sum(flow_data[:,1] == 9)
print("Flow meets this critera", flow_count1, " times in September before 2000")
print("The percentage of the critera is", flow_count1 / flow_count2)
# %%
