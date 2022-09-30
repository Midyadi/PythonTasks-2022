import numpy as np
from matplotlib import pyplot as plt

# Настройка гистограммы
plt.figure(figsize=(7, 6))
plt.title('Gauss 2D')

# Получение данных
np.random.seed(34)
data = np.random.normal(32, 1, size=10000)
x = data[:5000]
y = data[5000:]

# Построение данных
x_edges = np.linspace(28, 36, 101)
y_edges = np.linspace(28, 36, 101)
distribution, x_edges, y_edges = np.histogram2d(x, y, bins=(x_edges, y_edges))

cs = plt.matshow(distribution)
plt.colorbar(cs)

# Сохранение
plt.savefig('Gauss 2D.jpg')