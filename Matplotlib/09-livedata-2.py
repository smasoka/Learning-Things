import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


# Dynamic
x_vals = []
y_vals = []
index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    
    plt.cla()
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.tight_layout()    
    plt.legend(loc='upper left')
    

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()


