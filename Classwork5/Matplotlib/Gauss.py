import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl

# Настройка шрифта
mpl.rcParams['font.size'] = 16

# Настройка графика
plt.figure(figsize=(7, 6))
plt.title('Gauss')
plt.xlabel("Events")
plt.ylabel("Value")

# Получение данных
np.random.seed(34)
data = np.random.normal(32, 1, size=10000)

# Построение данных
plt.hist(data, 'auto', label='Normal')

# Сохранение
plt.savefig('Gauss.jpg')
