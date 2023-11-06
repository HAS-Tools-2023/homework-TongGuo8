# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl 
# %%
filename = 'streamflow_week10.txt'
# %%
data=pd.read_table(filename, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                   index_col='datetime', parse_dates =['datetime']
        )
# %%
two_month_data = data[(data.index.month <= 11) & (data.index.month >= 10) & (data.index.year == 2023)]
Nov_flow = data[data.index.month == 11]
Nov_data_after2010 = data[(data.index.month == 11) & (data.index.year >= 2010)]
Nov_data_5th_11th_after2010 = data[(data.index.month == 11) & (data.index.year >= 2010) 
                                   & (data.index.day >= 5) & (data.index.day <= 11)]
mean_flow_5th_11th_yearly = Nov_data_5th_11th_after2010.resample("Y")['flow'].mean()
max_flow_5th_11th_yearly = Nov_data_5th_11th_after2010.resample("Y")['flow'].max()
min_flow_5th_11th_yearly = Nov_data_5th_11th_after2010.resample("Y")['flow'].min()
quantile_flow_5th_11th_yearly = Nov_data_5th_11th_after2010.resample("Y")['flow'].quantile(0.25)
# Pick data during 12th to 18th in November after 2010
Nov_data_12th_18th_after2010 = data[(data.index.month == 11) & (data.index.year >= 2010) 
                                   & (data.index.day >= 12) & (data.index.day <= 18)]
mean_flow_12th_18th_yearly = Nov_data_12th_18th_after2010.resample("Y")['flow'].mean()
max_flow_12th_18th_yearly = Nov_data_12th_18th_after2010.resample("Y")['flow'].max()
min_flow_12th_18th_yearly = Nov_data_12th_18th_after2010.resample("Y")['flow'].min()
# %%
# One week forecast
fig, ax = plt.subplots(2,2, figsize = (20,15))
ax = ax.flatten()
ax[0].scatter(Nov_data_after2010.index, Nov_data_after2010['flow'], label='daily flow', marker='x',color='darkcyan')
ax[0].set(title='Flow in November after 2010',
          xlabel='date',ylabel='flow')
ax[0].legend()
ax[1].plot(mean_flow_5th_11th_yearly, 
           marker='P',label='mean flow', color='green')
ax[1].plot(max_flow_5th_11th_yearly, 
           marker='*',label='max flow', color='purple')
ax[1].plot(min_flow_5th_11th_yearly,
           marker='s',label='min flow',color='pink')
ax[1].set(title='Mean flow from 5th to 11th in November after 2010',
          xlabel='year',ylabel='flow')
ax[1].legend()
ax[2].hist(Nov_data_5th_11th_after2010['flow'], 
           bins=20, alpha=0.5, histtype='stepfilled', 
           label='count',color='orange', edgecolor='blue')
ax[2].set(title='Flow count during 5th to 11th of November after 2010',xlabel='flow',ylabel='count')
ax[2].legend()
ax[3].plot(two_month_data.index, two_month_data['flow'],marker='P',
           label='daily flow', color='maroon')
ax[3].set(title='Flow in Oct & Nov in 2023', xlabel='datetime',ylabel='flow')
ax[3].legend()
week1_forecast= round(mean_flow_5th_11th_yearly.iloc[-4:-1].mean(),2)
print('One week forecast is', week1_forecast, 'cfs')

# %%
# Two week forecast
fig, ax = plt.subplots(1,3, figsize = (25,10))
ax = ax.flatten()
ax[0].scatter(Nov_data_12th_18th_after2010.index, Nov_data_12th_18th_after2010['flow'], label='daily flow', marker='X',color='yellowgreen')
ax[0].set(title='Flow in November after 2010',
          xlabel='date',ylabel='flow')
ax[0].legend()
ax[1].plot(mean_flow_12th_18th_yearly, 
           marker='P',label='mean flow', color='tomato')
ax[1].plot(max_flow_12th_18th_yearly, 
           marker='*',label='max flow', color='blue')
ax[1].plot(min_flow_12th_18th_yearly,
           marker='s',label='min flow',color='black')
ax[1].set(title='Mean flow from 12th to 18th in November after 2010',
          xlabel='year',ylabel='flow')
ax[1].legend()
ax[2].hist(Nov_data_12th_18th_after2010['flow'], 
           bins=20, alpha=0.5, histtype='stepfilled', 
           label='count',color='pink', edgecolor='blue')
ax[2].set(title='Flow count during 12th to 18th of November after 2010',xlabel='flow',ylabel='count')
ax[2].legend()
week2_forecast=round(mean_flow_12th_18th_yearly.loc['2016-12-31':'2021-12-31'].mean(),2)
print('Two week forecast is', week2_forecast, 'cfs')
# %%
# Tuesday exercise
### Exercise 1: 
# Given the following dataframe:
data = np.random.rand(4, 5)
def myadd(data):
    answer = np.mean(data, axis = 0)
    return(answer)
myadd(data)
# Write a function and use it to calculate the mean of every colum of the dataframe
# If you have time try doing it with and without a for loop (You can either use the function inside your fo loop or put a for loop inside your function)
def mean_columns(my_array):
    ncol= my_array.shape[1]
    col_mean=np.zeros(5)
    for i in range(ncol):
        col_mean[i]=np.mean(my_array[:,i])
    return(col_mean)
mean_columns(data)

def take_mean(some numbers):
    mean_number = np.mean(some numbers)
    return(mean_number)
mean_columns=np.zeros(5)
for i in range(data.shape[1]):
    mean_columns[i] = take_mean(data[:,i])
#%% Exercise two: regression analysis
iris_df = pd.read_csv('iris_df.csv', index_col='species')
# %%
# 1. How do you view the "unique" species in the `iris_df` index?
#hint use the function np.unique() and apply it to the index of the dataframe
np.unique(iris_df.index)
# %%
# 2. How do you "locate" only rows for the `versicolor` species?
#Hint use .loc to the rows that have the name 'versicolor'
vercolor = iris_df.loc['versicolor']
# %%
# 3. Calculate the mean for every column of the dataframe grouped by species. 
# look back at our pandas examples Use groupby.mean
mean_column = iris_df.groupby('species').mean()
iris_df.groupby(iris_df.index).mean()
# %%
# 4. Make a scatter plot of the `sepal length (cm)` versus the `petal length (cm)` for the `versicolor`` species?
#hit first grab out just the rows you want to plot 
#Then use scatter plot function to plot the columns you want (plotting notes)
ver_len_vs = vercolor[['sepal length (cm)','petal length (cm)']]
fig = plt.figure()
plt.scatter(ver_len_vs['sepal length (cm)'], ver_len_vs['petal length (cm)'], label='versicolor', marker='x',color='red')
plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')
plt.legend(loc='upper left')

ax = plt.axes()
ax.scatter(ver_len_vs['sepal length (cm)'], ver_len_vs['petal length (cm)'], label='versicolor', marker='x',color='red')
# 5.  Do the same plot for `setosa` and `virginica` all on the same figure. Color them 'tomato', 'darkcyan', and 'darkviolet', respectively. (BONUS: Try to write the code so you only need to type each iris name one time)
# %%
#Repeat what you did in 4 three times

setosa_col = iris_df.loc['setosa']
setosa_len_vs = setosa_col[['sepal length (cm)','petal length (cm)']]
virginica_col = iris_df.loc['virginica']
virginica_len_vs = virginica_col[['sepal length (cm)','petal length (cm)']]

ax = plt.axes()

ax.scatter(ver_len_vs['sepal length (cm)'], ver_len_vs['petal length (cm)'], label='versicolor', marker='x',color='tomato')
ax.scatter(setosa_len_vs['sepal length (cm)'], setosa_len_vs['petal length (cm)'], label='setosa', marker='x',color='darkcyan')
ax.scatter(virginica_len_vs['sepal length (cm)'], virginica_len_vs['petal length (cm)'], label='virginica', marker='x',color='darkviolet')
ax.legend()

# 6. Write a function that will do 'ax.scatter' for a given iris type and desired color of points and use this to function to modify the code you make in 5

#HINT no for loop needed, the function should have two arguments and you will call it 3 times. 
#Copy your code from #5 down here and replace your ax.scatter calls with your function. 
# %%
# Solution1
ax = plt.axes()
def color_name(index, color):
    ax.scatter(iris_df.loc[iris_df.index == index]['sepal length (cm)'], 
               iris_df.loc[iris_df.index==index]['petal length (cm)'], 
               label=index, marker='x', color = color)
    ax.legend()
ax.set(xlabel='sepal length (cm)', ylabel='petal length (cm)')

color_name(index= 'virginica', color='darkviolet')
color_name('versicolor','tomato')
color_name('setosa', 'darkcyan')
# %%
# Solution2 (the positions of ax=plt.axes, ax.legend are different)
def color_name(index, color):
    ax.scatter(iris_df.loc[iris_df.index == index]['sepal length (cm)'], 
               iris_df.loc[iris_df.index==index]['petal length (cm)'], 
               label=index, marker='x', color = color)
    
ax = plt.axes()
color_name(index= 'virginica', color='darkviolet')
color_name('versicolor','tomato')
color_name('setosa', 'darkcyan')
ax.set(xlabel='sepal length (cm)', ylabel='petal length (cm)')
ax.legend()
# Thursday exercise
# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. You should do this two ways: (1) by modifying the read.table function arguments directly. (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'], index_col='datetime',
                            parse_dates =['datetime'])

print(data.info())
data['datetime']=pd.to_datetime(data['datetime'])
data =data.set_index('datetime')
print(data.info())
# Exercise 2: 
# %%
#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 
daymet = pd.read_csv('daymet.csv', sep=',', skiprows=1, names=['date', 'year',
                            'yday', 'dayl(s)', 'prcp (mm/day)','srad (W/m^2)','swe (kg/m^2)','tmax (deg c)','tmin (deg c)','vp (Pa)'], index_col='date',
                             parse_dates =['date'])
#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 
daymet.describe()
# %%
#2.3  Make a scatter plot of day length (dayl) vs maximum temperature.
ax = plt.axes()
ax.scatter(daymet['dayl(s)'], daymet['tmax (deg c)'], marker='*',label='tmax', color= 'brown', s=5)
ax.legend()
# %%
#2.4 Make a plot with three lines (1) average, (2) min and (3) max shortwave radiation (srad) vs the month of the year (i.e. 1-365)

daymet_after_2015= daymet[daymet.index.year >= 2015]
daymet_after_2015_monthly = daymet_after_2015.resample('M')['srad (W/m^2)']
srad_mean=daymet_after_2015_monthly.mean()
srad_min=daymet_after_2015_monthly.min()
srad_max=daymet_after_2015_monthly.max()
ax = plt.axes()
ax.plot(srad_mean, '-', color='blue',label='mean srad')
ax.plot(srad_max,'--',color='orange',label='max srad')
ax.plot(srad_min, ':', color='green',label='min srad' )
ax.set(xlabel='month of every year after 2015', ylabel='srad value')
ax.legend()  