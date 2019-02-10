# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:56:01 2019

Introduction to data science course on coursera

@author: chloe.chou
"""

############################
# Function
############################

def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

############################
# Check type
# [tuple cannot be altered, but list can]
############################


x = (1, 'a', 2, 'b')
type(x)


x = [1,3,4,5]
type(x)

x.append(6)
print(x)



############################
# Loop & While
############################


# loop & while
for i in x:
    print(i)
    
    
i=0
while(i != len(x)):
    print(x[i])
    i = i + 1

# concate list
[1,2] + [3,4]

# repeat
[1]*3


############################
# Check element in list
############################

1 in [1,2,3]
import re
re.search("Chloe", "Chloe Chou", re.IGNORECASE)!=None

'Christopher Arthur Hansen Brooks'.split(' ')[0]
'Christopher Arthur Hansen Brooks'.split(' ')[-1]


############################
# Dictionary (keys, values)
############################


x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Christopher Brooks'] # Retrieve a value by using the indexing operator

# get the email
for name in x:
    print(x[name])

for email in x.values():
    print(email)
for name in x.keys():
    print(name)

for name, email in x.items():
    print(name+" : "+email)

# Unpack a sequence into different variables
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x


############################
# time (current time & previous date)
############################

import time
import datetime
time.time()
dtnow = datetime.datetime.fromtimestamp(time.time())
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second
"%s-%02d-%s" %(dtnow.year, dtnow.month, dtnow.day)

(datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")



############################
# lambda
############################

my_function = lambda a, b, c : a + b
my_function(1,2,3)


############################
# iterate
############################
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
my_list

my_list = [number for number in range(0,1000) if number % 2 == 0]
