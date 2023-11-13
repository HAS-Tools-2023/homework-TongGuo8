# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl 
# %%
filename = 'streamflow_week11.txt'
# %%
data=pd.read_table(filename, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                   index_col='datetime', parse_dates =['datetime']
        )
# %%
# First pick the data in November in all years, after 2010 and in 2023
Nov_data_2023 = data[(data.index.month == 11) &  (data.index.year == 2023)]
Nov_flow = data[data.index.month == 11]
Nov_data_after2010 = data[(data.index.month == 11) & (data.index.year >= 2010)]
# Pick data during 12th to 18th in November after 2010
Nov_data_12th_18th_after2010 = data[(data.index.month == 11) & (data.index.year >= 2010) 
                                   & (data.index.day >= 12) & (data.index.day <= 18)]
mean_flow_12th_18th_yearly = Nov_data_12th_18th_after2010.resample("Y")['flow'].mean()
max_flow_12th_18th_yearly = Nov_data_12th_18th_after2010.resample("Y")['flow'].max()
min_flow_12th_18th_yearly = Nov_data_12th_18th_after2010.resample("Y")['flow'].min()
# Pick flow data from 19th to 25th in November after 2010
Nov_data_19th_25th_after2010 = data[(data.index.month == 11) & (data.index.year >= 2010) 
                                   & (data.index.day >= 19) & (data.index.day <= 25)]
mean_flow_19th_25th_yearly = Nov_data_19th_25th_after2010.resample("Y")['flow'].mean()
max_flow_19th_25th_yearly = Nov_data_19th_25th_after2010.resample("Y")['flow'].max()
min_flow_19th_25th_yearly = Nov_data_19th_25th_after2010.resample("Y")['flow'].min()

# %%
# One week forecast
fig, ax = plt.subplots(2,2, figsize = (20,15))
ax = ax.flatten()
ax[0].scatter(Nov_data_12th_18th_after2010.index, Nov_data_12th_18th_after2010['flow'], 
              label='daily flow', marker='X',s=50,color='orange')
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
ax[3].plot(Nov_data_2023.index, Nov_data_2023['flow'],marker='P',
           label='daily flow', color='maroon')
ax[3].set(title='Flow of Nov in 2023', xlabel='datetime',ylabel='flow')
ax[3].legend()
week1_forecast=round(max_flow_12th_18th_yearly.loc['2016-12-31':'2021-12-31'].mean(),2)
print('One week forecast is', week1_forecast, 'cfs')


# %%
# Two week forecast
fig, ax = plt.subplots(3,1, figsize = (20,20))
ax = ax.flatten()
ax[0].scatter(Nov_data_after2010.index, Nov_data_after2010['flow'], label='daily flow', marker='x',color='darkcyan')
ax[0].set(title='Flow in November after 2010',
          xlabel='date',ylabel='flow')
ax[0].legend()
ax[1].plot(mean_flow_19th_25th_yearly, 
           marker='P',label='mean flow', color='green')
ax[1].plot(max_flow_19th_25th_yearly, 
           marker='*',label='max flow', color='purple')
ax[1].plot(min_flow_19th_25th_yearly,
           marker='s',label='min flow',color='pink')
ax[1].set(title='Mean flow from 5th to 11th in November after 2010',
          xlabel='year',ylabel='flow')
ax[1].legend()
ax[2].hist(Nov_data_19th_25th_after2010['flow'], 
           bins=20, alpha=0.5, histtype='stepfilled', 
           label='count',color='cyan', edgecolor='blue')
ax[2].set(title='Flow count during 5th to 11th of November after 2010',xlabel='flow',ylabel='count')
ax[2].legend()


pick_data1= round(mean_flow_19th_25th_yearly.loc['2020-12-31':'2022-12-31'].mean(),2)
pick_data2=round(mean_flow_19th_25th_yearly.loc['2016-12-31':'2018-12-31'].mean(),2)
week2_forecast=(pick_data1 + pick_data2) / 2
print('Two week forecast is', week2_forecast, 'cfs')