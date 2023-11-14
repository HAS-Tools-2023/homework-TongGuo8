# Starter code for week 6 Pandas

# %%
# Import the modules we will use
import os
import pandas as pd
import matplotlib.pyplot as plt
#LC deleting packages that aren't being used (np & mpl)


# %%
# ** MODIFY ** #LC get rid of this since you don't want me to modify
# Set the file name and path to where you have stored the data
filename = 'streamflow_week8.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

# %%
# Timeseries
# LC see linter notes about adding white space around comments and operators
data2 = pd.read_table(filepath, sep='\t', skiprows=31,
        names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'], parse_dates=['datetime'])
# print(data.info()) # LC - note this line doesn't work
print(data2.info())


# %%
# LC -- this needs a comment describing whats happening 
datai = data2.set_index('datetime')  # LC note you can do thiw withink your read statement if you want. 
datai.head() 

# LC - try not to name your variables 'test' try to name them something more descriptive 
test = datai[datai.index.month == 10]  # LC note I added spaces around the '=' per the linter
test2 = datai[(datai.index.month == 10) & (datai.index.year == 2023)]
fig, ax = plt.subplots(figsize=(15,10))
ax.plot(test['flow'])
# %%
# One week forecast
# LC need comment explaining how this works. 
test3 = datai[(datai.index.month == 10) & (datai.index.year >= 2010)]
data_y2=test.resample("Y")['flow'].mean()
test4 = datai[(datai.index.month == 10) & 
              (datai.index.year >= 2010) & 
              (datai.index.day >= 22) & 
              (datai.index.day <=28)]
data_y3 = test4.resample("Y")['flow'].mean()
pre_data=data_y3.loc['2019-12-31':'2021-12-31'].mean()

# LC - add some white space to break it up
# plots
print('One week forecast is', pre_data, 'cfs')
fig, ax = plt.subplots(2, 2, figsize=(20, 10))
ax = ax.flatten() 
ax[0].plot(test2['flow'], marker='P', label='daily flow', color='green')
ax[0].legend()
ax[0].set(title='Daily flow in October 2023', xlabel='datetime',
          ylabel='count')

# LC add comment here (eg. subplot 1)
ax[1].hist(test3['flow'], bins=40, alpha=0.5, histtype='stepfilled',
           label='count', color='orange', edgecolor='blue')
ax[1].legend()
ax[1].set(title='flow count in October after 2010', xlabel='datetime',
          ylabel='count')

#LC add comment here (e.g. subplot2)
ax[2].plot(data_y2, linestyle='--',color='rosybrown',label="flow")
ax[2].set(title="Mean Flow in October", xlabel="year",
          ylabel="Monthly Avg Flow [cfs]")
ax[2].legend()
data_w = test.resample("w")['flow'].mean()

#LC add comment here
ax[3].plot(data_w, 'D', color='olive',label='weekly flow')
ax[3].set(title="Mean Flow in October (weekly)", xlabel="datetime",
       ylabel="Weekly Avg Flow [cfs]")
ax[3].legend()

# %%
# Two week forecast
# LC need description here explaining wha tyou are doing
# LC note how I formatted these multi line calls to indent them so they are easier to read
lastday_Oct=datai[(datai.index.month == 10) & 
                  (datai.index.year >= 2010) & (datai.index.day >= 29)]
Nov_data= datai[(datai.index.month == 11) & 
                (datai.index.year >= 2010)]
Nov_data2=datai[(datai.index.month == 11) & 
                (datai.index.year >= 2010) & (datai.index.day <= 4)]
data_y4 = Nov_data2.resample("Y")['flow'].mean()
data_y5=lastday_Oct.resample("Y")['flow'].mean()

# LC add white space before plot 
# LC need a comment here 
fig, ax = plt.subplots(1,3,figsize=(18,6))
ax[0].plot(Nov_data['flow'], marker='x',color='blue',label='flow')
ax[0].set(title='Daily flow in November after 2010', ylabel='flow', xlabel='date')
ax[0].legend()

#LC insert a comment here on whats being plotted
ax[1].plot(data_y4, 's--', color='green',label='average flow')
ax[1].set(title='Mean flow from 1st to 4th in November after 2010', ylabel='flow', xlabel='year')
ax[1].legend()

#LC insert a comment here on whats being plotted
ax[2].plot(data_y5,':o', color='brown',label='average flow')
ax[2].set(title='Mean flow of last three days in October',xlabel='date',ylabel='flow')
ax[2].legend()

#LC -- this is analysis it should be separated with white space and with a comment
data_sum3 = Nov_data.resample("Y")['flow'].quantile(0.25)
pick_data1=data_y5.loc['2019-12-31':'2020-12-31'].mean()
pick_data2=data_y4.loc[['2017-12-31', '2018-12-31',
                         '2020-12-31','2021-12-31','2022-12-31']].mean()
forecast_data=(pick_data1+pick_data2) /2
print('Two week forecast is', forecast_data,'cfs')
# %%
# 

# %%
# LC - needs a comment
monthly_sum = test4.groupby(test4.index.year)['flow'].mean()
fig, ax =plt.subplots()
ax.bar(monthly_sum.index, monthly_sum.values,color='green')
# %%
