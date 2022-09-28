import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.size'] = 16
plt.figure(figsize=(11,7))

plt.title(r'$y = \sin x \cdot x^{-2}$')
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

x_data = np.linspace(0, 100, 11)
y_data = np.sin(x_data) * pow(x_data, -2 * (x_data > 0))

plt.plot(x_data, y_data, 'r^', label="Красивый график")

plt.grid(b=True, which='major', axis='both', alpha=1)
plt.grid(b=True, which='minor', axis='both', alpha=0.5)

plt.savefig('Graph Matplotlib(1-2).jpg')
