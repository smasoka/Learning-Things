#!/anaconda3/bin/python

import numpy as np
import matplotlib.pyplot as plt
# For 3D Ggraphs
from mpl_toolkits.mplot3d import Axes3D, axes3d

# Line 
# Scatter
# Histogram
# Bar
# 3D Graph (with an add-on library)

Xarray2d = np.random.random_sample( (4,5)) * 100
Xarray3d = np.random.random_sample( (3,4,5)) * 100
Yarray2d = 2*Xarray2d**2-3*Xarray2d+1
Yarray3d = 2*Xarray3d**2-3*Xarray3d+1
print(Xarray2d.shape, Yarray2d.shape)
print(Xarray2d)
print(Yarray2d)
#print("3D")
#print(Xarray3d)
#print(Yarray3d)

# Start plotting

# 1. Line
plt.plot(Xarray2d.T, Yarray2d.T)
plt.xlabel('X random values')
plt.ylabel('Y function (of X) values')
plt.title('Line Graph')
# ??? HOW TO WORK THE LEGEND FOR ARRAYS ????
#plt.legend(('label1', 'label2', 'label3', 'label4', 'label5'))
plt.show()

# 2. Scatter
plt.scatter(Xarray2d.T, Yarray2d.T)
plt.xlabel('X random values')
plt.ylabel('Y function (of X) values')
plt.title('Scatter Graph')
# ??? HOW TO WORK THE LEGEND FOR ARRAYS ????
#plt.legend(('label1', 'label2', 'label3', 'label4', 'label5'))
plt.show()

# 3. Histogram
# for col in Xarray.axis()
plt.hist(Xarray2d.T[0], Yarray2d.T[0])
plt.xlabel('X random values')
plt.ylabel('Y function (of X) values')
plt.title('Histogram Graph')
# ??? HOW TO WORK THE LEGEND FOR ARRAYS ????
#plt.legend((),('label1', 'label2', 'label3', 'label4', 'label5'))
plt.show()

# 4. Bar Graph
plt.bar(Xarray2d.T[0], Yarray2d.T[0])
plt.xlabel('X random values')
plt.ylabel('Y function (of X) values')
plt.title('Bar Graph')
# ??? HOW TO WORK THE LEGEND FOR ARRAYS ????
#plt.legend(('label1', 'label2', 'label3', 'label4', 'label5'))
plt.show()

# 5. Pie Graph
plt.pie(Yarray2d[0])
plt.title('Pie Graph')
# ??? HOW TO WORK THE LEGEND FOR ARRAYS ????
#plt.legend((),('label1', 'label2', 'label3', 'label4', 'label5'))
plt.show()


# Something Else
x = np.arange(0., 5., 0.2)
print(x)
# red dashes, blue squares and green triangles
plt.plot(x, x, 'ro', label='Red O')
plt.plot(x, x**2, 'bs', label='Blue Square') 
plt.plot(x, x**3, 'g^', label='Green Star')
plt.xlabel("Range of X")
plt.ylabel("Rang of Y (function of X)")
plt.title("Interesting Plot")
plt.legend()
plt.show()


