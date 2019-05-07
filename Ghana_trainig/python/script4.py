#!/anaconda3/bin/python

import math
import cmath
import random

x = 12
# MATH
print(math.sqrt(x))
print(math.sin(x))
print(math.cos(x))
print(math.pi)
print(math.e)
# CMATH
complexa = 3 - 2j
print(cmath.sqrt(complexa))
#RANDOM
print(random.random() * 100)
print(int(random.random() * 100))
print(random.randint(100, 150))
# For loop range - random
for i in range(10):
    print(random.randint(1,101))
x = []
for i in range(50):
    x.append(random.randint(1,101))
print(x[-5:])

# y = x^2 - x 
# For each value of x (x is a list), calculate a corresponding value of y, where y = x^2 - x or ....
y = []
for xi in x:
    y.append(xi**2 - xi)
print(y[-5:])
# y = sqrt(x^3) + 2x
y_sin = []
for xi in x:
    y_sin.append(math.sqrt(xi**3) + 2*xi)
print(y_sin[-5:])








