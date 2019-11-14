#!/anaconda3/bin/python

import math
import cmath as cm
from math import sqrt
from sys import argv

# Functions
# Inputs
# Script Arguments

def add(x,y):
    print("This is function add")
    return x+y

def add2(*args):
    print(args)
    ans = 0
    for arg in args:
        ans += arg
    return ans

def sub(x,y):
    return x - y

my_ans = add(5,7)
print('my_ans = ',my_ans) 
my_ans = sub(23, 45)
print('my_ans = ', my_ans)

#print(add(3,5,8))
print(add2(3,4,5,7))

# Get input from User
#input1 = int(input("Please enter your input 1 : "))
#input2 = int(input("Please enter your second input: "))
#print(add2(input1,input2))

for arg in argv:
    print(arg)

print(argv[1])
input1 = int(argv[1])
input2 = int(argv[2])
print(type(input1))

print(add2(input1,input2))







