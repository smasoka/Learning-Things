import numpy as np
import matplotlib.pyplot as plt


N = 5
menMeans = (20, 35, 0, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
xMeans = (25, 32, 34, 20, 25)
yMeans = (25, 30, 45, 15, 20)

menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
xStd = (3, 5, 2, 3, 3)
yStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)
p3 = plt.bar(ind, xMeans, width,
             bottom=womenMeans, yerr=xStd)
p4 = plt.bar(ind, yMeans, width,
             bottom=xMeans, yerr=yStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()