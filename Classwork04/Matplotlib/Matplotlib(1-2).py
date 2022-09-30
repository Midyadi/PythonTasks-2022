import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Настройка шрифта
mpl.rcParams['font.size'] = 16

# Настрока графика
plt.figure(figsize=(11, 7))
plt.title(r'$y = \sin x \cdot x^{-2}$')
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

# Построение данных
x_data = np.linspace(0, 100, 11)
y_data = np.sin(x_data) * pow(x_data, -2 * (x_data > 0))

plt.plot(x_data, y_data, 'r^')

# Настрока сетки
plt.grid(b=True, which='major', axis='both', alpha=1)
plt.grid(b=True, which='minor', axis='both', alpha=0.5)

# Cохранение
plt.savefig('Graph Matplotlib(1-2).jpg')
