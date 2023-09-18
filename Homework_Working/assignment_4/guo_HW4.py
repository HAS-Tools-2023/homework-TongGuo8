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
# Starter Code
# Count the number of values with flow > 105.97 and month ==9
flow_count = np.sum((flow_data[:,3] > 105.97) & (flow_data[:,1]==9))
flow_count_all = np.sum(flow_data[:,1] == 9)
criteria = (flow_data[:, 3] > 105.97) & (flow_data[:, 1] == 9)
pick_data = flow_data[criteria, 3]
flow_mean = np.mean(pick_data)

# Calculate the average flow for these same criteria 

flow_mean = np.mean(flow_data[(flow_data[:,3] > 105.97) & (flow_data[:,1]==9)])

print("Flow meets this critera", flow_count, " times in September")
print('The percentage of the critera is', flow_count / flow_count_all)
print('And has an average value of', flow_mean, "when this is true")
# %%
# Count the number of values with flow > 105.97 and month ==9 before 2000
flow_count1 = np.sum((flow_data[:,3] > 105.97) & (flow_data[:,0] <= 2000) & (flow_data[:,1]==9))
criteria1 = (flow_data[:, 3] > 105.97) & (flow_data[:, 1] == 9) & (flow_data[:,0] <= 2000)
pick_data = flow_data[criteria1, 3]
flow_mean = np.mean(pick_data)
flow_count2 = np.sum((flow_data[:,0] <= 2000) & (flow_data[:,1] == 9))
flow_mean1 = np.mean(flow_data[(flow_data[:,3] > 105.97) & (flow_data[:,0] <= 2000) & (flow_data[:,1]==9)])

print("Flow meets this critera", flow_count1, " times in September before 2000")
print("The percentage of the critera is", flow_count1 / flow_count2)
print('And has an average value of', flow_mean1, "when this is true")

# %%
# Count the number of values with flow > 105.97 and month ==9 after 2010
flow_count3 = np.sum((flow_data[:,3] > 105.97) & (flow_data[:,0] >= 2010) & (flow_data[:,1]==9))
criteria2 = (flow_data[:, 3] > 105.97) & (flow_data[:,0] >= 2010) & (flow_data[:, 1] == 9) 
pick_data = flow_data[criteria2, 3]
flow_mean = np.mean(pick_data)
flow_count4 = np.sum((flow_data[:,0] >= 2010) & (flow_data[:,1] == 9))
flow_mean2 = np.mean(flow_data[(flow_data[:,3] > 105.97) & (flow_data[:,0] >= 2010) & (flow_data[:,1]==9)])

print("Flow meets this critera", flow_count3, " times in September after 2010")
print("The percentage of the critera is", flow_count3 / flow_count4)
print('And has an average value of', flow_mean2, "when this is true")

# %%
# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=20)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# %%
# The flow in September 17th - 23rd after 2010 
flow_in_Sep = (flow_data[(flow_data[:,0] >= 2010) & (flow_data[:,2] >= 17) & (flow_data[:,2] <= 23) & (flow_data[:,1]==9),3])
mybins = np.linspace(0, 500, num=15) 
plt.hist(flow_in_Sep, bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# %%
# The flow in September after 2010
flow_in_Sep2 = (flow_data[(flow_data[:,0] >= 2010) & (flow_data[:,1]==9),3])
mybins = np.linspace(0, 500, num=10) 
plt.hist(flow_in_Sep2, bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# %%
# The flow in September before 2000
flow_in_Sep3 = (flow_data[(flow_data[:,0] <= 2000) & (flow_data[:,1]== 9),3])
print(np.max(flow_in_Sep3), np.min(flow_in_Sep3))
mybins = np.linspace(np.min(flow_in_Sep3), 1000, num=15) 
plt.hist(flow_in_Sep3, bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# %%
# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants = np.nanquantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants)

# The quantlies of flow in September 17th- 23rd after 2010
flow_quants1 = np.nanquantile(flow_in_Sep, q=[0, 0.25, 0.5, 0.9])
print('The quantlies of flow in September 17th- 23rd after 2010:', flow_quants1)

# The quantlies of flow in September after 2010
flow_quants2 = np.nanquantile(flow_in_Sep2, q=[0, 0.25, 0.5, 0.9])
print('The quantlies of flow in September after 2010:', flow_quants2)

# The quantlies of flow in September before 2000
flow_quants3 = np.nanquantile(flow_in_Sep3, q=[0, 0.25, 0.5, 0.9])
print('The quantlies of flow in September before 2000:', flow_quants3)



# %%

# %%
