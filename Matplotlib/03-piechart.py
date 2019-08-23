import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
# plt.xkcd()
# print(plt.style.available)

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
explode = [0,0,0,0.1,0]

# slices = [60,40, 30, 20]
# labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

plt.pie(slices[:5], labels=labels[:5], explode=explode, shadow=True, 
        startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
plt.title('Most Popular Languages')
plt.tight_layout()
plt.show()    