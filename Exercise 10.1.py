from __future__ import print_function, division

import random

# creating list
nestedList = [1, 2, ['b', 2], 3]

# indexing list: the sublist has now been accessed
subList = nestedList[2]

# access the first element inside the inner list:
element = nestedList[2][0]

print("List inside the nested list: ", subList)
print("First element of the sublist: ", element)

#Exercise 10.1. Write a function called nested_sum.

def sum_nest_lst(lst):
         t=0
         for l in lst:
             if(type(l)==int):
                 t=t+l
             if(type(l)==list):
                 t=t+sum(l)
         print(t)

def nested_sum(t):

    sum=0
    for i in t:
        if isinstance(i, list):
            for j in i:
                sum +=j
        else:
            sum += i
    return sum