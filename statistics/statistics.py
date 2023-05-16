"""
Using pandas to read data from excel then analysing it with kstest
"""
import pandas
import matplotlib.pyplot as plt
from scipy import stats
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data_1 = pandas.read_excel(os.path.join(__location__, 'experiment_1.xlsx'))
df_1 = pandas.DataFrame(data_1)
data_2 = pandas.read_excel(os.path.join(__location__, 'experiment_2.xlsx'))
df_2 = pandas.DataFrame(data_2)
data_3 = pandas.read_excel(os.path.join(__location__, 'experiment_3.xlsx'))
df_3 = pandas.DataFrame(data_3)

df_1['experiments'].plot(kind='bar')
plt.show()
df_2['experiments'].plot(kind='bar')
plt.show()
df_3['experiments'].plot(kind='bar')
plt.show()

print(df_1.describe())
print(df_2.describe())
print(df_3.describe())

df_1.plot.kde()
plt.show()
df_2.plot.kde()
plt.show()
df_3.plot.kde()
plt.show()

d_1 = df_1['experiments']
print(stats.kstest(d_1, 'norm', (d_1.mean(), d_1.std()), N=5000))

d_2 = df_2['experiments']
print(stats.kstest(d_2, 'norm', (d_2.mean(), d_2.std()), N=5000))

d_3 = df_3['experiments']
print(stats.kstest(d_3, 'norm', (d_3.mean(), d_3.std()), N=5000))
