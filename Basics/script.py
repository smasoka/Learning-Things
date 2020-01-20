import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

width = .35 # width of a bar

m1_t = pd.DataFrame({
 'Rainfall' : [81.2, 274.8, 60, 0.4, 0, 0, 0, 0, 1.4, 78.6, 60.2],
 'Months of the Year' : ['Feb', 'Marc', 'April', 'May', 'June',
                         'July', 'Aug','Sept', 'Oct',
                         'Nov', 'Dec'],
 'Temperature' : [23.6,22.7,21.7,21.1,17.5,15.7,18.9,22.9,26.5,24.7,24.5],
 })

x_indexes = np.arange(len(m1_t['Temperature']))

# m1_t[['Rainfall','Months of the Year']].plot(kind='bar', width = width)
# m1_t['Temperature'].plot(secondary_y=True)
rainfall = m1_t['Rainfall']
months = m1_t['Months of the Year']
temp = m1_t['Temperature']

plt.bar(x_indexes - width, rainfall, width=width)
plt.plot(temp)

ax = plt.gca()
# plt.xlim([-width, len(m1_t['Rainfall'])-width])
ax.set_xticklabels(('Feb', 'Mar', 'April', 'May', 'June',
                         'July', 'Aug','Sept', 'Oct',
                         'Nov', 'Dec'))
#ax.set_yticklabels('Temperature')
plt.title('Rainfall and Temperature in 2014')
plt.xlabel("Rainfall")
plt.ylabel("Temperature")
plt.tight_layout()
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
