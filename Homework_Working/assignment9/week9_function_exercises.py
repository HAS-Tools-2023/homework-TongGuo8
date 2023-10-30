# %%
# EXERCISE 1:
# Write a function that takes the month as input and returns the number of non-leap year days in that month as output

def myadd(a):
    if a == 1 or a == 3 or a == 5 or a == 7 or a== 8 or a == 10 or a == 12:
        answer = 31
        return(answer)
    elif a == 2:
        answer=28
        return(answer)
    else:
        answer = 30
        return(answer)
myadd(9)
# %%
# EXERCISE 2:
# Write a function that takes takes your streamflow dataframe and one other user defined variable as an input and returns some metric of interest

# %%
## Exercise 3:
# Write a function to create one of your figures from the previous homework
