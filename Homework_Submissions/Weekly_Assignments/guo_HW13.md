#### Name: Tong Guo
#### Date: 11/26/2023
#### Assignment_13

### Grade 
9/9 : Really nice work on this. You have made great improvements from your last script to this one!  I like all the functions you have defined and your documentation is much improved. 

Glad you found chatGPT to be useful. It takes some practice to figure out how to make the best use of it but once you get the hang of it can make a lot of things easier especially documentation. 

I left you some comments for how you can improve your script a bit just for future reference.  One big picture comment is to define all of your functions at the top of the script and make sure that if your functions are relying on any data that that data is included as an argument to the function. 

### Forecast:
| Forecast | Flow(cfs) |
| ----------- | ----------- |
| **one week** | *189.31* |
| **two week** | *200.62* |

1. **The forecast analysis**

- In my script, I first plot the mean, maximum and minimum flow of the same period as forecast week, and the plot shows the flow in 2019 are extermely higher than other years, so when wrting the forecast function, I first pick up and calculated the same period mean and minimun flow of every year, but I used the mean flow of the minimum flow of all years after 2010 as my forecast which can aviod the flow being increased high due to the high flow in 2019. 

2. **About ChatGPT**
- ChatGPT is really amazing! I can get the answer what my script needs and can run as I can describe my request properly, and ChatGPT can provide some functions I didn't know before, for example, `pd.Timestamp()`, this is really useful in my second function when I want to use the month and day from the simple input date format. It is much convienient for me to know and how to use new functions by asking ChatGPT, and using it can save a lot of time!
- And it is helpful to give me about some doc srtings of my functions, I can based on the giving answers to adjust some content of it.
- The ChatGPT mainly improves my original script readability, so that's what I changed some name of my function names.