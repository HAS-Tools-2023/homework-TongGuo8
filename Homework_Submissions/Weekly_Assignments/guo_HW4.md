Name: Tong Guo
Data: 09/28/2023
Assignment_4

##
## Grade
3/3 
- see the comment in the previous HW about formatting as a markdown file. 
- exercise 3.1 was my mistake, you are correct it should be a 3X3 array
##

Reason: According to the quantiles of flow in September after 2010, most the daily recharge are less than 182, and half of the flow data are less than 97.9. The histogram shows most of flow are between 50-150.
I calculate the quantiles of flow between 17th and 23rd in September after 2010, the results shows half of the data are less than 97.9.   
I also calulate the quantiles of flow for September 2023 and the results shows 50% and 75% values are less than 105 and 143.8 respectively.
Based on the results above, I think the forecast of the first week should be more than 100 but not too much, which my first week forecast is 105.97, and the second week forecast is 97.9.

Questions:
1. According to the quantiles, I can know how many data are less than what value, and the value of 0.5 quantiles can help me decide the specific value of forecasting. 
The histogram can display the counts of the flow data between different section directly. For example in the hisotgram of flow in September, I can know the flow between 50-100 counts has most , and the second is 100-150. This can let me know the range of predicted values to choose from.
2. Flow data is an array. It is composed of float64, the dimension of it is 2, and the size is 50672. 
3. There were 585 days of the daily flow greater than my prediction of 105.97 in September, and the percentage is 56.96%.
4. There were 281 days of the daily flow greater than my prediction of 105.97 in September before 2000, the percentage is 78.06%.
There were 191 days of the daily flow greater than my prediction of 105.97 in September after 2010, the percentage is 48.11%.
5. The flow decreases in the first half of September and increase in the beginning of the second half, then decreases.
6. In the exercise 3.1, I can use np.arange function to bulid an array has values 0-9, but how to use reshape function to build a 3x2 array from np.arange(10)? Because I use reshape directly which shows it can't reshape a 3x2 array from np.arange(10), so I use np.random.randint function.
