# %%
# This set of exercises works through
# some basic python functionality
# I'll still be using some functions from 
# numpy but nothing you write should need it
# although you can use it if you'd like
import numpy as np

# %%  1.)
# Write code to translate a boolean value
# to a string using a conditional statment.
#  Specifically, if the `testval` 
# is `True` then print "Yes" and if it is
# `False` then print "No"
testval = bool(np.random.choice([0, 1]))
# TODO: Your code here
if testval :
    print('Yes')
else:
    print('No')
message = None
# ...
print(message)

#1.b Can you translate this to a string without a conditional statement?
print
# %% 2.)
#Given the following list write print statements that spell the word 
#'bad' as many ways as possible by pulling from mylist
mylist = ['a', 'b', 'c', 'd']
print(mylist[1]+mylist[0]+mylist[3])
print(mylist[1], mylist[0], mylist[3])
# %% 3.)
# You will be given a random integer, and 
# your goal is to return the same value, but
# as a negative number. Notice, the number you
# are given may already be negative
testval = np.random.random_integers(-100, 100)
# TODO: Your code here
if testval >= 0:
    str('testval')
else:
    str('-testval')
    
negval = None
print(testval, negval)


# %% 3.)
# Time for a coding interview classic, FizzBuzz
# The rulse of the game:
#  - print numbers from 1 to 100
#  - if the number is divisible by 3 print "Fizz"
#  - if the number is divisible by 5 print "Buzz"
#  - if the number is divisible by both 3 and 5 print "FizzBuzz"
#  - otherwise, print the number
testvals = np.arange(1, 101)
#TODO: Your code here
# ...
print(testvals)
for n in testvals:
    if n % 3 == 0:
        print(n, 'is fizz')
    if n % 5 == 0:
        print(n, 'is buzz')
    if n % 3 == 0 and n % 5 == 0:
        print(n, 'is fizzbuzz')
    if n % 3 != 0 and n % 5 != 0:
        print(n)
for v in testvals:
    print('NONE')

# %%
