#### Name: Tong Guo
#### Date: 10/07/2023
#### Assignment_6

### Forecast:
| Forecast | Flow(cfs) |
| ----------- | ----------- |
| **one week** | **77.79** |
| **two week** | **88.95** |
> #### Reason: 
> #### I picked up the flow data the `month` is October and `year` larger 2010, `day` before 15. The mean, min and max flow are 154.70cfs, 55.7cfs and 1910cfs. And 0.25, 0.5 and 0.75 quantiles are 91.53cfs, 120.0cfs and 144.75cfs respectively.
> #### I grouped the flow data by `year`, and calculated the mean, max and min flow, from the results I found that the minimun flow of October is in 2023, and the mean flow of October in 2023 also has the lowest flow, which means in 2023 the flow might not be much lower than the previous years, and the year of 2019 and 2020 have the similar values as 2023, so I chose the mean flow of 2019 and 2020 and average them as the one week forecast, which is 77.79cfs.
> #### And I ues the same way to forecast the two week forecast, but I change `day` after 15, the flow is obviously increase than the half October, I also chose the 2019 and 2020 mean flow, which is 88.95cfs.
 ### Assignment Questions:
1. **Provide a summary of the data frames properties.**
    
 | Column | Type |
 | ----------- | ----------- |
 | agency_cd | object |
 | site_no | int64 |
 | datetime | object|
 | flow | float64 |
 | code | object |
 | year | int32 |
 | month | int32 |
 | day | int32 |
RangeIndex(start=0, stop=12695, step=1)
2. **Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.**

|  | flow |
 | ----------- | ----------- |   
| count | 12695.000000 |     
| mean | 352.544797 |       
| std | 1463.166047 |           
| min | 19.000000 |           
| 25% | 93.000000 |          
| 50% | 157.000000 |           
| 75% | 215.000000 |           
| max | 63400.000000 |

3. **Provide the same information but on a monthly basis**
                                                                   
| month | count | mean | std | min | 25% | 50% | 75% | max |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |     
| 1 | 1084.0 | 694.385609| 2642.701653 | 158.0 | 202.000 | 220.0 | 314.00 | 63400.0 |
| 2 | 988.0 | 877.008097 | 3208.739869 | 136.0 | 199.000 | 238.0 | 612.50 | 61000.0 |
| 3 | 1085.0 | 1064.491244 | 2416.095415 | 97.0 | 180.000 | 378.0 | 1070.00 | 42200.0 |
| 4 | 1050.0 | 323.222857 | 584.313196 | 64.9 | 111.000 | 141.0 | 218.75 | 4690.0 |
| 5 | 1085.0 | 103.845991 | 49.928918 | 39.9 | 76.600 | 92.0 | 118.00 | 546.0 |
| 6 | 1050.0 |   65.066762 |   28.191344 |  22.1 |  48.325 |  60.0 |   76.00 | 481.0 |  
| 7 |     1085.0 |  105.943871 |  214.174556 |  19.0 |  52.000 |  70.0 |  110.00 | 5270.0 |   
| 8 |     1085.0 |  170.843687 |  288.914361 |  29.6 |  78.000 | 116.0 |  178.00 | 5360.0 |  
| 9 |     1050.0 |  166.601810 |  274.594973 |  37.5 |  86.150 | 117.0 |  166.00 | 5590.0 |   
| 10 |    1059.0 |  145.004533 |  111.053856 |  55.7 | 106.000 | 126.0 |  153.00 | 1910.0 |   
| 11 |    1020.0 |  199.985294 |  225.677357 | 117.0 | 153.000 | 171.5 |  197.00 | 4600 | 
| 12 |    1054.0 |  330.376660 | 1052.000260 | 153.0 | 189.000 | 203.0 |  225.00 | 28700.0 |

4. **Provide a table with the 5 highest and 5 lowest flow values for  the period of record.** 

| | datetime | month | flow |
| ----------- | ----------- | ----------- | ----------- |
| 5885  | 2005-02-12 |     2 | 35600.0 |
| 12497 | 2023-03-22 |     3 | 42200.0 |
| 2235 |  1995-02-15 |     2 | 45500.0 |
| 1510 |  1993-02-20 |     2 | 61000.0 |
| 1467  | 1993-01-08 |    1  |63400.0 |
| 8581 |  2012-07-01 |     7 |    19.0 |
| 8582 |  2012-07-02 |     7 |    20.1 |
| 8580 |  2012-06-30 |     6 |    22.1 |
| 8579 |  2012-06-29 |     6 |    22.5 |
| 8583 |  2012-07-03 |    7  |   23.4 |

5. **Provide a list of historical dates with flows that are within 10% of your week 1 forecast value for the month of September.**

|   |   agency_cd | site_no  |  datetime | flow | code | year | month | day |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | 
| 123 |       USGS | 9506000 | 1989-05-05 | 83.0    A | 1989 |     5 |   5 |
| 124 |       USGS | 9506000 | 1989-05-06 | 86.0    A | 1989 |     5 |   6 |
| 125 |       USGS | 9506000 | 1989-05-07 | 80.0    A | 1989 |     5 |   7 |
| 126 |       USGS | 9506000 | 1989-05-08 | 81.0    A | 1989 |     5 |   8 |
| 127 |       USGS | 9506000 | 1989-05-09 | 81.0    A | 1989 |     5 |   9 |
...         ...      ...         ...   ...  ...   ...    ...  ...
| 12655 |     USGS | 9506000 | 2023-08-27 | 86.8    P | 2023 |     8 |  27 |
| 12666 |     USGS | 9506000 | 2023-09-07 | 88.4    P | 2023 |     9 |   7 |
| 12667 |     USGS | 9506000 | 2023-09-08 | 80.5    P | 2023 |     9 |   8 |
| 12672 |     USGS | 9506000 | 2023-09-13 | 80.4    P | 2023 |     9 |  13 |
| 12678 |     USGS | 9506000 | 2023-09-19 | 81.9    P | 2023 |     9 |  19 |

[1080 rows x 8 columns]
