# %%
# Import the packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import urllib.request as req
import urllib
# %%
# Use the rest API to get the data of site 09506000
# The data is from 1989-01-01 to 2023-11-25
url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no=09506000" \
        "&referred_module=sw&period=&begin_date=1989-01-01&end_date=2023-11-25"

data = pd.read_table(url, skiprows=30, names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                     parse_dates=['datetime'], index_col=['datetime'])


# %%
# Write the function to plot the mean, max and min flow yearly
# of any period after 2010
flow_periods = (12, 3, 9)

# This is a tricky function I like it! One suggestion though. You are relying on 'data' inside the function but you are not passing it as an argument into the function which requires the user to know this and already have that object created. I would suggest adding the dataframe as an argument to your function. 
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
    # Select the data after 2010
    data_after_2010 = data[data.index.year >= 2010]
    # Pick the same date period flow date
    pick_data = data_after_2010[(data_after_2010.index.month == month)&
                               (data_after_2010.index.day >= date1) & 
                               (data_after_2010.index.day <= date2)]
    # Get the mean, max and min line of the pick_data
    ax.plot(pick_data.resample("Y")['flow'].mean(), label='mean flow')
    ax.plot(pick_data.resample("Y")['flow'].max(), label='max flow')
    ax.plot(pick_data.resample("Y")['flow'].min(), label='min flow')

ax = plt.axes()
flow_period(flow_periods[0],flow_periods[1],flow_periods[2])
ax.set(xlabel='Time', ylabel='Flow', title='Mean, max and min flow')
ax.legend()

# %%
# The function can get the forecast and plot for any week
# LC - This is great! Next time pull the out to the top block of the code after the import statements so its easy for the user to find. 
forecast_date= ('2023-12-1', '2023-12-2') # Users can change the start and end date here

# LC - next time define all of your functions at the top of the code in one block that makes the script a little easier to follow. 
def forecast_date_input(start, end):
    """
    Generates a forecast for the flow based on a specified time period.

    Parameters:
    - start (str): Start date in 'YYYY-MM-DD' format.
    - end (str): End date in 'YYYY-MM-DD' format.

    Returns:
    - float: Forecasted flow value.

    Notes:
    - 'data' should have a DateTimeIndex.
    - If the input end date is earlier than '2023-11-25', 
      the function calculates the flow of the period directly 
      and plots the daily data and forecasted data.
    - If the input end date is later than '2023-11-25', 
      it calculates the mean and minimum flow of the same period in previous years
      (after 2010 and exclude 2019). 
      The mean result of minimum flow is considered the forecast value.
      It plots the mean flow of the same period in every year after 2010 
      and the forecast flow.
    - The function can only calculate the flow in the same month,
      the start and end date should have same month number.
    """
    # Convert the input date strings into timestamp
    start_date = pd.Timestamp(start) 
    end_date = pd.Timestamp(end)

    # If the input end date is earlier than our last date
    # calculate the flow of the period directly,
    # and plot the daily data and forecast data.
    if end_date <= pd.Timestamp('2023-11-25'):
        # Select the data of the period
        forecast_week = data[(data.index >= start) & (data.index <= end)]
        # Calculate the mean flow of the period
        # Using round() keep 2 decimal places
        forecast = round(np.mean(forecast_week['flow']), 2)

        # Plot the daily flow scatters and forecast line
        ax.scatter(forecast_week.index, forecast_week['flow'], marker='s',
               color='green', label= 'Flow of previous years')
        ax.axhline(y= forecast, label='Forecast', color='red')
        print('The forecast is', forecast ,'cfs')
        return forecast
    # If the input end date is later than the lastest day of our available data
    # Calculate the flow of the same period of previous years (after 2010)
    # The result is the forecast value.
    else:
        pick_data = data[(data.index.year >= 2010) 
                         &(data.index.month == start_date.month) 
                         &(data.index.day >= start_date.day) & 
                         (data.index.day <= end_date.day)]
        # Resample the pick data by year and calculate the mean and flow
        # and plot the mean flow data in figure
        pick_data_min_yearly = pick_data.resample('Y')['flow'].min()
        pick_data_mean_yearly = pick_data.resample('Y')['flow'].mean()
        # Calculate the 
        forecast2 = round(pick_data_min_yearly.mean(),2)

        # Draw the same period mean flow after 2010 in plot as scatter
        # and the forecast flow as the line 
        ax.scatter(pick_data_mean_yearly.index, pick_data_mean_yearly.values, 
                   marker='s', color='green', label= 'Mean flow of previous years')
        ax.axhline(y=forecast, label='Forecast', color='red')
        print('The forecast is',forecast ,'cfs')
        return forecast


ax = plt.axes()  
forecast_date_input(forecast_date[0],forecast_date[1])
ax.set(xlabel='Time', ylabel='Flow', 
       title='Forecast and historical flow in the same week')
ax.legend()

# %%
# If the week spans two months
# input two flow forecasts in different month
# Calculate the mean value of two periods flow

# LC Its great you are considering this case (i.e. when a forecast could span two months). I would suggest in having this be a condition that gets checked for and corrected for in your original function though rather than expecting the user to know and correct for it. 
two_period_flows = (170.15, 208.46) # Enter two mean flow in a week but include two months

def two_period_flow(flow1, flow2):
    """
    Calculates the mean flow forecast when a week spans two months.

    Parameters:
    - flow1 (float): Flow forecast for the first period.
    - flow2 (float): Flow forecast for the second period.

    Returns:
    - float: Mean flow forecast calculated from the input forecasts.

    Notes:
    - If the week spans two months, and flow forecasts are available
      for each period, this function calculates the mean value of 
      the flow forecasts for both periods.
    """
    forecast = round((flow1 + flow2) / 2, 2)
    print('The forecast is', forecast, 'cfs')
    return forecast
# For example: the forecast of 2023/11/26-2023/12/2,
# The forecast flow of 11/26-11/30 is 170.15, and 12/1-12/2 is 208.46
# Using function to get one forecast of the whole week
two_period_flow(two_period_flows[0], two_period_flows[1])
# %%



# %%
