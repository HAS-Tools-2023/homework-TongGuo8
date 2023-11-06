## Exercises for thursday's class

# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a datetime object. You should do this two ways: (1) by modifying the read.table function arguments directly. (2) keeping the read.table line I have below the same and modifying the dataframe after the fact. 
# How can you check to confirm that what you did worked? 
data = pd.read_table('streamflow_demo.txt', sep='\t',skiprows=30, names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'])



# Exercise 2: 

#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as the index and making sure to treat that column as a datetime object. 

#2.2: Explore this dataset and report what variables it contains, what date ranges are covered and the frequency of the data. 


#2.3  Make a scatter plot of day length (dayl) vs maximum temperature. Fit a trend line 


#2.4 Make a plot with three lines (1) average, (2) min and (3) max shortwave radiation (srad) vs the day of the year (i.e. 1-365)

