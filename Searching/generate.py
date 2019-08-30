import numpy as np 

# 1 million integers (1 D)
data = np.random.randint(low=1, high=1000000, size=1000000)
np.savetxt('1_d.csv', data)