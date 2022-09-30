import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Настройка шрифта
mpl.rcParams['font.size'] = 16

# Настройка графика
plt.figure(figsize=(6, 6))
plt.title(r'$e ^{-x \cdot \sin x}$')
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.ylim(0, 5)

# Построение данных
x_data = np.linspace(10, 100, 1001)
y_data = np.exp(-x_data * np.sin(x_data))

plt.plot(x_data, y_data)

# Настройка сетки
plt.grid(b=True, which='major', axis='both', alpha=1)
plt.grid(b=True, which='minor', axis='both', alpha=0.5)
plt.minorticks_on()

# Cохранение
plt.savefig('Graph Matplotlib(3-5).jpg')
