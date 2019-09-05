import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
# plt.xkcd()
# print(plt.style.available)


# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
    
#     language_counter = Counter()
    
#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))
        
# print(language_counter)
# print(language_counter.most_common(15))

# ----- PANDAS WAY --------- #

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for resp in lang_responses:
    language_counter.update(resp.split(';'))

languages = []
popularity = []

languages, popularity = map(list, zip(*language_counter.most_common(15)))
# for item  in language_counter.most_common(15):
#     languages.append(item[0])
#     popularity.append(item[1])

# print(languages)
# print(popularity)
languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)
plt.title('Most Popular Languages')
plt.xlabel('Number of People Who Use')
# plt.ylabel('Programming Languages')
# plt.legend()
plt.tight_layout()
# plt.savefig('plot.png')
plt.show()    