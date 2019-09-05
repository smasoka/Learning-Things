import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
# plt.xkcd()
# print(plt.style.available)

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [4, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [3, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [1, 1, 1, 1, 2, 2, 3, 3, 4]
player4 = [2, 6, 5, 5, 4, 2, 1, 1, 0]
player5 = [5, 1, 2, 2, 2, 4, 4, 4, 4]
player6 = [1, 1, 1, 1, 2, 2, 3, 3, 4]
player7 = [6, 6, 5, 5, 4, 2, 1, 1, 0]
player8 = [1, 1, 2, 2, 2, 4, 4, 4, 4]
player9 = [1, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player1','player2','player3']
colors = ['#6d904f', '#fc4f30', '#008fd5']

plt.stackplot(minutes, player1, player2, player3,player4,player5,player6,player7,player8,player9)
plt.title('Awesome Stack Plots')
# plt.legend(loc='lower left')
plt.legend(loc=(0.07, 0.05))
plt.tight_layout()
plt.show()    