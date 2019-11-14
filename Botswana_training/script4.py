#!/anaconda3/bin/python

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

# plt.plot(x,y)
# plt.title("A simple plot")
# plt.xlabel("PI values")
# plt.ylabel("sin(x)")
# plt.show()

x = np.arange(0,10,0.2)
y = 2*x**2 + 3*x + 1
# plt.plot(x,y,"*")
# plt.title("A simple plot 2")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.show()

# t = np.arange(0, 5, 0.2)
# plt.plot(t,t,'ro', t, t**2,'bs',t, t**3, 'g^')
# plt.show()
# explode = [0,0,0.1,0,0,0,0,0,0,0]
# labels = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# slices = np.random.randint(5050,6000,size=10)
# plt.pie(slices, explode=explode, labels=labels,\\
# autopct='%1.1f%%', shadow=True)
# plt.legend()
# plt.tight_layout()
# plt.title("Random pie values")
# plt.show()

ages = np.random.randint(10, 100, size=500)
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black')
plt.title("Ages of Respondents")
plt.xlabel("Ages")s
plt.ylabel("Total Respondents")
plt.legend()
plt.show()
