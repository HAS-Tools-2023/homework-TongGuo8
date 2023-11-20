# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json
import urllib.request as req
import urllib
# %%
# Write a function by inputting the site number, start and end date,
# using url to get Verde River streamflow


def streamflow(site, start, end):
    url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
        "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end
    data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                         parse_dates=['datetime'], index_col=['datetime'])
    return (data)


camp_verde = streamflow(site='09506000', start='1989-01-01', end='2023-11-18')
# First pick the data in November in all years, after 2010 and in 2023
Nov_flow = camp_verde[camp_verde.index.month == 11]
Nov_data_2023 = camp_verde[(camp_verde.index.month == 11) & 
                           (camp_verde.index.year == 2023)]
Nov_data_after2010 = camp_verde[(camp_verde.index.month == 11) & 
                                (camp_verde.index.year >= 2010)]
# Pick data during 19th to 25th in November after 2010
# Calculate the mean, max and min values of this period
Nov_data_19th_25th_after2010 = camp_verde[(camp_verde.index.month == 11) &
                                          (camp_verde.index.year >= 2010) &
                                          (camp_verde.index.day >= 19) & (camp_verde.index.day <= 25)]
mean_flow_19th_25th_yearly = Nov_data_19th_25th_after2010.resample("Y")['flow'].mean()
max_flow_19th_25th_yearly = Nov_data_19th_25th_after2010.resample("Y")['flow'].max()
min_flow_19th_25th_yearly = Nov_data_19th_25th_after2010.resample("Y")['flow'].min()
# Pick flow data from November 26th to December 2nd after 2010
# and also calculate the mean, max and min values of this period yearly
Nov_data_26th_30th_after2010 = camp_verde[(camp_verde.index.month == 11) & (camp_verde.index.year >= 2010)
                                          & (camp_verde.index.day >= 26)]
mean_flow_26th_30th_yearly = Nov_data_26th_30th_after2010.resample("Y")['flow'].mean()
max_flow_26th_30th_yearly = Nov_data_26th_30th_after2010.resample("Y")['flow'].max()
min_flow_26th_30th_yearly = Nov_data_26th_30th_after2010.resample("Y")['flow'].min()

Dec_data_1st_2nd_after2010 = camp_verde[(camp_verde.index.month == 12) & (camp_verde.index.year >= 2010)
                                        & (camp_verde.index.day <= 2)]
mean_flow_1st_2nd_yearly = Dec_data_1st_2nd_after2010.resample("Y")['flow'].mean()
max_flow_1st_2nd_yearly = Dec_data_1st_2nd_after2010.resample("Y")['flow'].max()
min_flow_1st_2nd_yearly = Dec_data_1st_2nd_after2010.resample("Y")['flow'].min()

# %%
# Reading the data of location latitude: 34.5494 and longtitude: -111.8441
url = "https://daymet.ornl.gov/single-pixel/api/data?lat=34.5491&lon=-111.8441"  \
    "&vars=prcp&start=2010-01-01&end=2023-11-17&format=json"
response = req.urlopen(url)
# Look at the keys and use this to grab out the data
responseDict = json.loads(response.read())
responseDict['data'].keys()
year = responseDict['data']['year']
yearday = responseDict['data']['yday']
precip = responseDict['data']['prcp (mm/day)']
# Make a dataframe from the data and groupby the data by year
data2 = pd.DataFrame({'year': year,
                     'yearday': yearday, "precip": precip})
precip2_daily = data2.groupby('year')['precip'].mean()
plt.plot(precip2_daily)



# %%
# The precipitation in another site
def prepcip(siteid, start, end):
    url = "https://nwis.waterdata.usgs.gov/nwis/uv?cb_00045=on&format=rdb&site_no=" + siteid +  \
        "&legacy=1&period=&begin_date=" + start + "&end_date=" + end
    prepcip_data = pd.read_table(url, skiprows=28, names=['agency_cd', 'site_no', 'datetime', 'tz_cd', '6727_00045',
                                                          '6727_00045_cd'], parse_dates=['datetime'], index_col=['datetime'])
    return (prepcip_data)


Granite_Creek = prepcip(
    siteid='09502960', start='2023-01-01', end='2023-11-18')
# Change the column name
Granite_Creek2 = Granite_Creek.rename(columns={'6727_00045': 'precipitation'})
# Resample the precipitation data by day and week
precip_daily = Granite_Creek2.resample('D')['precipitation'].mean()
precip_weekly = precip_daily.resample("w").mean()
ax = plt.axes()
ax.plot(precip_weekly, label='precipitation', color='green', linestyle='-.')
ax.set(xlabel='time', ylabel='precipitation')
ax.legend()
# %%
# Plot the flow of our forecast site and precipitation of another site
# in 2023
ax = plt.axes()
ax.plot(Nov_data_2023.index,
        Nov_data_2023['flow'], label='flow of 095060000', color='red')
ax.set(xlabel='Datetime', ylabel='Flow',
       title='Flow and precipitation variation in 2023')
ax1 = ax.twinx()
ax1.plot(precip_daily, color='grey', label='precipitation of 09502960')
ax1.set(ylabel='Precipitation')
ax.legend()
ax1.legend()
# %%
# The gage height of 095060000
# Using url to get the data after 2010
url = "https://nwis.waterdata.usgs.gov/usa/nwis/uv/?cb_00065=on&format=rdb&site_no=09506000&legacy=1&period=&begin_date=2010-01-01&end_date=2023-11-19"
gage_height = pd.read_table(url, skiprows=32, names=['agency_cd', 'site_no', 'datetime', 'tz_cd', '6765_00065',
                                                     '6765_00065_cd', '6766_00065', '6766_00065_cd'], parse_dates=['datetime'], index_col=['datetime'])
# Change the column name
gage_height2 = gage_height.rename(columns={'6766_00065': 'gage height'})
# Resample the data by day and week and calculate the mean value
gage_height_daily = gage_height2.resample('D')['gage height'].mean()
gage_height_weekly = gage_height2.resample('w')['gage height'].mean()
# Plot the weekly data
ax = plt.axes()
ax.plot(gage_height_weekly, color='yellowgreen', label='gage height')
ax.set(xlabel='Datetime', ylabel='Gage height',
       title='Weekly gage height variation of Verde River after 2010')
ax.legend()
# Pick the gage height in November
Nov_gage_height_after2010 = gage_height_daily[(gage_height_daily.index.month == 11)]
# Pick the gage height  in November 2023
Nov_gage_height_2023 = gage_height_daily[(gage_height_daily.index.month == 11) 
                                         & (gage_height_daily.index.year == 2023)]
# %%
# Draw Streamflow and gage height of 095060000 in November after 2010 in a plot
ax = plt.axes()
ax.plot(Nov_data_after2010.index,
        Nov_data_after2010['flow'], label='flow', color='red')
ax1 = ax.twinx()
ax1.plot(Nov_gage_height_after2010, color='blue', label='gage height')
ax.set(xlabel='Datetime', ylabel='Flow',
       title='Streamflow and gage height of Verde river in November after 2010')
ax1.set(ylabel='Gage height')
ax.legend(loc='upper left')
ax1.legend(loc='upper right')
# %%
# %%
# Plot streamflow data
# One week forecast
fig, ax = plt.subplots(2, 2, figsize=(30, 20))
ax = ax.flatten()
# Plot scatter flow from 19th to 25th in November after 2010 
ax[0].scatter(Nov_data_19th_25th_after2010.index, Nov_data_19th_25th_after2010['flow'],
              label='daily flow', marker='X', s=50, color='orange')
ax[0].set(title='Flow in November after 2010',
          xlabel='date', ylabel='flow')
ax[0].legend()
# Plot the average, maximum and minimum flow during 19th to 25th
# after 2010
ax[1].plot(mean_flow_19th_25th_yearly,
           marker='P', label='mean flow', color='tomato')
ax[1].plot(max_flow_19th_25th_yearly,
           marker='*', label='max flow', color='blue')
ax[1].plot(min_flow_19th_25th_yearly,
           marker='s', label='min flow', color='black')
ax[1].set(title='Mean flow from 19th to 25th in November after 2010',
          xlabel='year', ylabel='flow')
ax[1].legend()
# Plot the flow count during 19th to 25th in November
# after 2010
ax[2].hist(Nov_data_19th_25th_after2010['flow'],
           bins=20, alpha=0.5, histtype='stepfilled',
           label='count', color='maroon', edgecolor='blue')
ax[2].set(title='Flow count during 19th to 25th of November after 2010',
          xlabel='flow', ylabel='count')
ax[2].legend()
# Plot the daily flow in 2023 November
ax[3].plot(Nov_data_2023.index, Nov_data_2023['flow'], marker='P',
           label='daily flow', color='red')
ax[3].set(title='Flow of Nov in 2023', xlabel='datetime', ylabel='flow')
ax[3].legend()
# Calculate one week forecast
Oneweek_forecast = round(
    mean_flow_19th_25th_yearly.loc['2016-12-31':'2022-12-31'].mean(), 2)
print('One week forecast is', Oneweek_forecast, 'cfs')
# %%
# Two week forecast
fig, ax = plt.subplots(2, 1, figsize=(10, 20))
ax = ax.flatten()
# Plot the mean, max and min flow from 26th to 30th
# after 2010
ax[0].plot(mean_flow_26th_30th_yearly,
           marker='P', label='mean flow', color='green')
ax[0].plot(max_flow_26th_30th_yearly,
           marker='*', label='max flow', color='purple')
ax[0].plot(min_flow_26th_30th_yearly,
           marker='s', label='min flow', color='pink')
ax[0].set(title='Mean flow from 26th to 30th in November after 2010',
          xlabel='year', ylabel='flow')
ax[0].legend()
# Plot the mean, max and min flow from 1st to 2nd in December
# after 2010
ax[1].plot(mean_flow_1st_2nd_yearly,
           marker='P', label='mean flow', color='olive')
ax[1].plot(max_flow_1st_2nd_yearly,
           marker='*', label='max flow', color='grey')
ax[1].plot(min_flow_1st_2nd_yearly,
           marker='s', label='min flow', color='brown')
ax[1].set(title='Mean flow from 1st to 2nd in December after 2010',
          xlabel='year', ylabel='flow')
ax[1].legend()
# Pick the data in November and December
# Calculate the mean value of them to be two week forecast
pick_data1 = round(
    mean_flow_26th_30th_yearly.loc['2016-12-31':'2018-12-31'].mean(), 2)
pick_data2 = round(
    mean_flow_1st_2nd_yearly.loc['2016-12-31':'2018-12-31'].mean(), 2)
Twoweek_forecast = (pick_data1 + pick_data2) / 2
print('Two week forecast is', Twoweek_forecast, 'cfs')
# %%
# Exercise 1:


def streamflow(site, start, end):
    url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
        "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end
    data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                         parse_dates=['datetime'], index_col=['datetime'])
    ax.plot(data.index, data['flow'],
            label=site)
    ax.legend()
    return (data)


ax = plt.axes()
ax.set(xlabel='time', ylabel='flow')


streamflow(site='09506000',
           start='2022-10-16',
           end='2023-10-16')
# 09511300
streamflow(site='09511300',
           start='2022-10-16',
           end='2023-10-16')
# 09504950
streamflow(site='09504950',
           start='2022-10-16',
           end='2023-10-16')

# %%
# Exercise 1:


def streamflow(site, start, end):
    url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=" + site + \
        "&referred_module=sw&period=&begin_date=" + start + "&end_date=" + end
    data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                         parse_dates=['datetime'], index_col=['datetime'])
    ax.plot(data.index, data['flow'],
            label=site)
    ax.legend()
    return (data)


ax = plt.axes()
ax.set(xlabel='time', ylabel='flow')


streamflow(site='09506000',
           start='2022-10-16',
           end='2023-10-16')
# 09511300
streamflow(site='09511300',
           start='2022-10-16',
           end='2023-10-16')
# 09504950
streamflow(site='09504950',
           start='2022-10-16',
           end='2023-10-16')
# Exercise 2:
mytoken = '8c0ae275729848549e22c9665e6fe321'
base_url = "http://api.mesowest.net/v2/stations/timeseries"
args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum',
    'stids': 'QVDA3',
    'units': 'metric',
    'token': mytoken}
apiString = urllib.parse.urlencode(args)
fullUrl = base_url + '?' + apiString
response = req.urlopen(fullUrl)
responseDict = json.loads(response.read())
responseDict['STATION'][0].keys()

dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']

data = pd.DataFrame({'Precipitation': precip}, index=pd.to_datetime(dateTime))

data_daily = data.resample('D').max()
plt.plot(data_daily, color='purple', label='max precip')
plt.xlabel('Datetime')
plt.ylabel('Precipation')
plt.title('Maximum precipitation')
plt.legend()
