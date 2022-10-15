import os
import psutil
import random as rnd
import sys

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')

# Пункт 1
print('Пункт 1')
new_diamonds = diamonds[(diamonds['x'] > 5) | (diamonds['y'] > 5) | (diamonds['z'] > 5)]
print(new_diamonds, '\n')

# Пункт 2
print('Пункт 2')
diam = pd.DataFrame()
for column in diamonds.columns:
    if diamonds[column].dtype == float:
        diam[column] = diamonds[column]
print(diam, '\n')

# Пункт 3
print('Пункт 3')
print(pd.DataFrame({"Mean": diam.mean()}), '\n')

# Пункт 4
print('Пункт 4', 'См. картинку Price.jpg', sep='\n')
price = pd.DataFrame(diamonds.groupby(['cut']).agg(Price=('price', 'mean')))
print(price, '\n')

x_data = price.index.values
y_data = price['Price'].values

matplotlib.rcParams['font.size'] = 19
price.plot(kind='bar', figsize=(10, 16))
plt.title("График")
plt.xlabel('cut')
plt.ylabel('price')
plt.ylim((3400, 4750))
plt.savefig("Price.jpg")

# Пункт 5
print('Пункт 5', 'См. картинку carat.jpg', sep='\n')
matplotlib.rcParams['font.size'] = 16

plt.figure(figsize=(8, 6))
plt.title('Graph')
plt.xlabel("Carat")
plt.ylabel("Amount")
plt.xlim((0, 3))

data = diamonds['carat']
plt.hist(data, 'auto')
plt.savefig('carat.jpg')

# Пункт 6
print('\nПункт 6')
for column in diamonds.columns:
    mask = diamonds.isna()[column]
    print(column, len(diamonds[mask].index.values))

# Пункт 7
print('\nПункт 7')
notna = diamonds.dropna()
print(notna, '\n')

# Пункт 8
print('Пункт 8')
print(sys.getsizeof(notna))

process = psutil.Process(os.getpid())
print(process.memory_info().rss)

# Пункт 9
print('\nПункт 9')
print(diamonds.loc[sorted(rnd.sample(range(53940), 20))])
