import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Настройки шрифта
mpl.rcParams['font.size']=16

# Настройки графика
plt.figure(figsize=(9,7))
plt.title(r'$e ^{x \cdot \sin x}$')
plt.xlabel("Ось X")
plt.ylabel("Логарифмическая ось Y")
plt.yscale('log')

# Построение данных
x_data = np.linspace(10,100,500)
y_data = np.exp(x_data*np.sin(x_data))
plt.plot(x_data,y_data, 'b^', label = r'$e ^{x \cdot \sin x}$')

# Настройки сетки
plt.grid(b=True, which='major', axis='both', alpha=1)
plt.grid(b=True, which='minor', axis='both', alpha=0.5)
plt.minorticks_on()

# Легенда
plt.legend()

# Сохранение
plt.savefig('Graph Matplotlib(6,8-9).jpg')