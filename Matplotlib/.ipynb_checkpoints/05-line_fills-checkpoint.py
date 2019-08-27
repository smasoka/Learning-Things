import pandas as pd
from matplotlib import pyplot as plt


data = pd.read_csv('salaries.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

overall_median = 57287

plt.plot(ages,dev_salaries, color='#444444', linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, label='Python')

# plt.fill_between(ages, py_salaries, overall_median, 
#                  where=(py_salaries > overall_median), 
#                  interpolate=True, alpha=0.25)

# plt.fill_between(ages, py_salaries, overall_median, 
#                  where=(py_salaries <= overall_median), 
#                  interpolate=True, alpha=0.25)

# or 
plt.fill_between(ages, py_salaries, dev_salaries, 
                 where=(py_salaries > dev_salaries), 
                 interpolate=True, alpha=0.25, label='Above Avg')

plt.fill_between(ages, py_salaries, dev_salaries, 
                 where=(py_salaries <= dev_salaries), 
                 interpolate=True, alpha=0.25, label='Below Avg')

plt.title('Median Salary by Age')
plt.xlabel('Ages')
plt.ylabel('USD')
plt.legend()
plt.tight_layout()
plt.show() 