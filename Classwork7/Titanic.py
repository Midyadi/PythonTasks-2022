import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic_with_nan = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")
titanic = titanic_with_nan.dropna(subset=['age'], axis=0).reset_index(drop=True)
print(titanic)

# Пункт 1
print('\nПункт 1')
clas = titanic.groupby(['class']).mean(numeric_only=True).round(2)
age = titanic.groupby(['age']).mean(numeric_only=True).round(2)
print(clas, age, sep='\n\n')

# Пункт 2
print('\nПункт 2')

mp3 = titanic[(titanic['class'] == 'Third') & (titanic['sex'] == 'male')].sort_values(by='age').reset_index(drop=True)
mp2 = titanic[(titanic['class'] == 'Second') & (titanic['sex'] == 'male')].sort_values(by='age').reset_index(drop=True)
mp1 = titanic[(titanic['class'] == 'First') & (titanic['sex'] == 'male')].sort_values(by='age').reset_index(drop=True)

fp3 = titanic[(titanic['class'] == 'Third') & (titanic['sex'] == 'female')].sort_values(by='age').reset_index(drop=True)
fp2 = titanic[(titanic['class'] == 'Second') & (titanic['sex'] == 'female')].sort_values(by='age').reset_index(
    drop=True)
fp1 = titanic[(titanic['class'] == 'First') & (titanic['sex'] == 'female')].sort_values(by='age').reset_index(drop=True)

border_age_mp3 = mp3.loc[mp3.shape[0] // 2]['age']
border_age_mp2 = mp2.loc[mp2.shape[0] // 2]['age']
border_age_mp1 = mp1.loc[mp1.shape[0] // 2]['age']

border_age_fp3 = fp3.loc[fp3.shape[0] // 2]['age']
border_age_fp2 = fp2.loc[fp2.shape[0] // 2]['age']
border_age_fp1 = fp1.loc[fp1.shape[0] // 2]['age']

min_age_mp3, max_age_mp3 = mp3['age'].min(), mp3['age'].max()
min_age_mp2, max_age_mp2 = mp2['age'].min(), mp2['age'].max()
min_age_mp1, max_age_mp1 = mp1['age'].min(), mp1['age'].max()

min_age_fp3, max_age_fp3 = fp3['age'].min(), fp3['age'].max()
min_age_fp2, max_age_fp2 = fp2['age'].min(), fp2['age'].max()
min_age_fp1, max_age_fp1 = fp1['age'].min(), fp1['age'].max()

print(f'Male 3rd class: {min_age_mp3} - {border_age_mp3}, {border_age_mp3} - {max_age_mp3}')
print(f'Male 2nd class: {min_age_mp2} - {border_age_mp2}, {border_age_mp2} - {max_age_mp2}')
print(f'Male 1st class: {min_age_mp1} - {border_age_mp1}, {border_age_mp1} - {max_age_mp1}', '\n')
print(f'Female 3rd class: {min_age_fp3} - {border_age_fp3}, {border_age_fp3} - {max_age_fp3}')
print(f'Female 2nd class: {min_age_fp2} - {border_age_fp2}, {border_age_fp2} - {max_age_fp2}')
print(f'Female 1st class: {min_age_fp1} - {border_age_fp1}, {border_age_fp1} - {max_age_fp1}')

# Пункт 3
print('\nПункт 3')
alive_mp3_young = mp3[mp3['age'] < border_age_mp3]['survived'].mean()
alive_mp3_old = mp3[mp3['age'] >= border_age_mp3]['survived'].mean()
alive_mp2_young = mp2[mp2['age'] < border_age_mp2]['survived'].mean()
alive_mp2_old = mp2[mp2['age'] >= border_age_mp2]['survived'].mean()
alive_mp1_young = mp1[mp1['age'] < border_age_mp1]['survived'].mean()
alive_mp1_old = mp1[mp1['age'] >= border_age_mp1]['survived'].mean()

alive_fp3_young = fp3[fp3['age'] < border_age_fp3]['survived'].mean()
alive_fp3_old = fp3[fp3['age'] >= border_age_fp3]['survived'].mean()
alive_fp2_young = fp2[fp2['age'] < border_age_fp2]['survived'].mean()
alive_fp2_old = fp2[fp2['age'] >= border_age_fp2]['survived'].mean()
alive_fp1_young = fp1[fp1['age'] < border_age_fp1]['survived'].mean()
alive_fp1_old = fp1[fp1['age'] >= border_age_fp1]['survived'].mean()

print(f'Male 3rd class: young - {alive_mp3_young.round(3)}, old - {alive_mp3_old.round(3)}')
print(f'Male 2nd class: young - {alive_mp2_young.round(3)}, old - {alive_mp2_old.round(3)}')
print(f'Male 1st class: young - {alive_mp1_young.round(3)}, old - {alive_mp1_old.round(3)}')
print(f'Female 3rd class: young - {alive_fp3_young.round(3)}, old - {alive_fp3_old.round(3)}')
print(f'Female 2nd class: young - {alive_fp2_young.round(3)}, old - {alive_fp2_old.round(3)}')
print(f'Female 1st class: young - {alive_fp1_young.round(3)}, old - {alive_fp1_old.round(3)}')

# Пункт 4
print('\nПункт 4')
mean_age_m = titanic[(titanic['sex'] == 'male') & (titanic['survived'] == 1)]['age'].mean().round(2)
mean_age_f = titanic[(titanic['sex'] == 'female') & (titanic['survived'] == 1)]['age'].mean().round(2)
print('Male:', mean_age_m)
print('Female:', mean_age_f)

# Пункт 5
print('\nПункт 5')
pandas_srotkl = titanic[titanic['survived'] == 1]['age'].std().round(3)
numpy_srotkl = np.std(list(titanic[titanic['survived'] == 1]['age'])).round(3)
print(pandas_srotkl, numpy_srotkl)  # Отличаются

# Пункт 6
print('\nПункт 6', 'См. картинку Survive.jpg', sep='\n')
data = titanic.groupby(['age'])['survived'].mean()

plt.figure()
plt.title("Survive")
plt.xlabel("age")
plt.ylabel("Rate")

plt.grid(visible=True, which='both')
plt.plot(data, 'r')
plt.minorticks_on()

plt.savefig("Survive.jpg")

# Пункт 7
print('\nПункт 7', 'См. картинку Survive(sex).jpg', sep='\n')
data_male = titanic[titanic['sex'] == 'male'].groupby(['age'])['survived'].mean()
data_fem = titanic[titanic['sex'] == 'female'].groupby(['age'])['survived'].mean()

plt.figure()
plt.title("Survived")
plt.xlabel("age")
plt.ylabel("Rate")

plt.grid(visible=True, which='both')
plt.plot(data_male, 'r', label='Male')
plt.plot(data_fem, 'b', label='Female')
plt.legend()
plt.minorticks_on()

plt.savefig("Survive(sex).jpg")

# Пункт 8
print('\nПункт 8')
summ = titanic['fare'].sum()
print(summ)
