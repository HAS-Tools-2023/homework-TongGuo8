# %%
# Import the packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json
import urllib.request as req
import urllib
# %%
# Use the rest API to get the data of 09506000
# From 1989-01-01 to 2023-11-25
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000" \
        "&referred_module=sw&period=&begin_date=1989-01-01&end_date=2023-11-22"
data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col=['datetime'])
# %%
# Write the function to plot the mean, max and min flow yearly
# of any period after 2010
data_after2010 = data[data.index.year >= 2010] # Select the data after 2010

def flow_period(month, date1, date2):
        """
    Plots the mean, max, and min flow data for a specific month and date range.

    Parameters:
    - month (int): The month for which the data will be selected (1-12).
    - date1 (int): The starting day of the date range.
    - date2 (int): The ending day of the date range.

    Note:
    - The function assumes 'data_after2010' is available in the global scope.
    - 'data_after2010' should have a DateTimeIndex.

    Example:
    flow_period(month=11, date1=25, date2=30) selects flow data for November
    from the 25th to the 30th and plots mean, max, and min flow.
    """
    pick_data = data_after2010[(data_after2010.index.month == month)&
                               (data_after2010.index.day >= date1) & 
                               (data_after2010.index.day <= date2)]
   
    ax.plot(pick_data.resample("Y")['flow'].mean(), label='mean flow')
    ax.plot(pick_data.resample("Y")['flow'].max(), label='max flow')
    ax.plot(pick_data.resample("Y")['flow'].min(), label='min flow')

ax = plt.axes()
flow_period(month= 11, date1= 25, date2 =30)
ax.set(xlabel='Time', ylabel='Flow', title='Mean, max and min flow')
ax.legend()
# %%
# The function can get the forecast and plot for any week
start = input('2023-11-1')
end = input('2023-11-7')
def forecast_date(start, end):
    forecast_week = data[(data.index >= start) & (data.index <= end)].resample('Y')['flow']
    forecast = round(forecast_week.mean(),2)

    ax.scatter(forecast_week, 's', color='green', label= 'Flow of previous years')
    ax.axhline(y= forecast, label='Forecast', color='red')

print('The forecast from', start, 'to', end, 'is', forecast, 'cfs.')
ax = plt.axes()
ax.set(xlabel='Time', ylabel='Flow', title='Forecast and historical flow in the same week')
ax.legend()
# %%
