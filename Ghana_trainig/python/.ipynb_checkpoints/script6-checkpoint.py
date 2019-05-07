#!/anaconda3/bin/python

import numpy as np
import pandas as pd

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
print(type(c))
c = []
for i in range(len(a)):
    c.append(a[i]+b[i])
print(c)
# Numpy
aa = np.array([1,2,4])
bb = np.array([4,5,6])
cc = aa + bb
print(cc)
print(type(cc))

print(np.arange(10))
print(np.arange(20, 50, 2))
print(np.linspace(20, 1000, 50))

dd = np.random.randint(40, 100, size=10)
print(dd)
print(dd.sum())
print(dd.mean())
print(np.median(dd))
print(np.std(dd))
print(np.var(dd))
print(dd.min())
print(dd.max())

print(np.sqrt(dd))
print(np.sort(dd))
print(np.flip(dd, axis=0))

array2d = np.array([ [1,2,3], [4,5,6] ])
print(array2d)
print(array2d.shape)
print(array2d.ndim)
print(array2d.size)
print(array2d.sum(axis=0))
print(array2d.sum(axis=1))

array2d = np.random.random_sample( (3,3)) * 100
array2d2 = np.random.random_sample( (3,3)) * 100
print(array2d)
print(array2d.sum())
print(array2d.sum(axis=0))
print(array2d.sum(axis=1))

print("array transpose")
print(array2d.transpose())
print("h Stack")
print(np.hstack([array2d,array2d2]))
print("v stack")
print(np.vstack([array2d,array2d2]))
print("dot operation")
print(array2d.dot(array2d2))
# 3 dimension
print("3D array")
array3d = np.random.random_sample( (3,4,5)) * 100
print(array3d)
print(array3d.shape)
print(array3d.ndim)
print(array3d.size)

# Look up "np.savetxt" function from numpy and learn how it works. 
# Use 'savetxt' to save an array or list
# Use 'ls' and 'cat' to view the new file created

np.savetxt("myarray.txt", array2d, delimiter=" , ")
np.savetxt("myarray3.txt", array3d.reshape((3,-1)), delimiter=" , ")

# Loading files using numpy 

data = np.loadtxt("myarray.txt", delimiter=" , ")
print(type(data))
print(data.shape)
print(data)

staff = np.loadtxt("staff.txt", delimiter=" ", dtype=str)
print(staff)
print(type(staff))


















