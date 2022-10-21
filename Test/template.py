import random as rnd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


def task1():
    return int(input()) ** 2 + int(input()) ** 2


def task2():
    string = input()
    k = 0
    for i in string:
        if i.islower():
            k += 1
    return k


def task3():
    string = input().split()
    k = 0
    for i in string:
        if 'sus' in i:
            k += 1
    return k


def task4(generator):
    gen = filter(lambda x: 'usu' in x, generator)
    return gen


def task5(list_of_smth):
    return list_of_smth[4:-5:5]


def task6(list1, list2, list3, list4):
    set1, set2, set3, set4 = set(list1), set(list2), set(list3), set(list4)
    set14 = set1.intersection(set4)
    set23 = set2.intersection(set3)
    set1234 = set14.union(set23)
    return set1234


def task7():
    np.random.seed(7)
    lst = np.array([rnd.randint(0, 26) for _ in range(25)], (5, 5))
    lst = lst.reshape((5, 5))
    minor = np.linalg.det(lst[1:][:4])
    return lst


def task8(f, min_x, max_x, N, min_y, max_y):
    x_data = np.linspace(min_x, max_x, N)
    y_data = f(x_data)

    plt.figure(figsize=(7, 6))
    plt.title('Task8')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.ylim((min_y, max_y))
    plt.xscale('log')
    plt.grid(visible=True, which='major', axis='both', alpha=1)
    plt.grid(visible=True, which='minor', axis='both', alpha=0.5)
    plt.minorticks_on()

    plt.plot(x_data, y_data, '.')

    dx = x_data[1] - x_data[0]
    diff = np.gradient(y_data, dx)

    plt.plot(x_data, diff)

    plt.savefig('function.jpg')


#############
def task9(data, x_array, y_array, threshold):
    plt.figure(figsize=(7, 6))
    plt.title('Task8')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.hist(data)
    plt.savefig('histograms_0.png')


################

def task10(list_of_smth, n):
    for i in range(len(list_of_smth)):
        newlist = list_of_smth[i:(i + n + 1) * ((i + n + 1) <= len(list_of_smth)) + len(list_of_smth) * (
                    (i + n + 1) > len(list_of_smth))]
        list_of_smth[i] = np.mean(newlist)
    return list_of_smth


def task11(filename="infile.csv"):
    df = pd.read_csv('infile.xlsx')
    for column in df.columns:
        print(column, ':', df[column].isna().sum())
    df['x'] = df['x'].interpolate()
    df['x_err'] = df['x_err'].fillna(df['x_err'].mean())
    df = df.dropna()
    print(df)

    plt.figure(figsize=(7, 6))
    plt.title('Task11')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(visible=True, which='major', axis='both', alpha=1)
    plt.grid(visible=True, which='minor', axis='both', alpha=0.5)
    plt.minorticks_on()
    plt.errorbar(df['x'], df['y'], xerr=df['x_err'], yerr=df['y_err'], fmt='o', ecolor='black', linestyle='None')
    plt.savefig('dataframe.pdf')


def task12(filename="video-games.csv"):
    csv = pd.read_csv('video-games.csv')
    info = dict()
    info['n_games'] = csv.shape[0]
    year = csv.groupby('year')['title'].count()
    info['by_years'] = year
    info['mean_price'] = csv[csv['publisher'] == 'EA']['price'].mean()
    info['age_max_price'] = (csv.groupby('age_raiting')[['price', 'title']].max())['title']
    info['mean_raiting_1_2'] = csv[(csv['max_players'] == 1) | (csv['max_players'] == 2)]['review_raiting'].mean()
    info['min_max_price'] = csv.groupby('age_raiting').agg(Max_price=('price', 'max'), Min_price=('price', 'min'),
                                                           Mean_sale=('sales_metric', 'mean')).sort_values(by='Max_price')
    info['n_games_by_age'] = pd.DataFrame(csv.groupby('review_raiting')['title'].count())
    info['max_raiting_by_years'] = pd.DataFrame((csv.groupby('year')[['review_raiting','title']].max())['title'])
    info['creators'] = set((','.join(list(csv['publisher'].dropna()))).split(','))
    return info


print(task12()['creators'])
