import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.size']=16
plt.figure(figsize=(6,6))

plt.title(r'$e ^{-x \cdot \sin x}$')
plt.xlabel("Ось X")
plt.ylabel("Ось Y")

x_data = np.linspace(10,100,1001)
y_data = np.exp(-x_data * np.sin(x_data))

plt.plot(x_data, y_data, label="Ещё один красивый график")

plt.grid(b=True, which='major', axis='both', alpha=1)
plt.grid(b=True, which='minor', axis='both', alpha=0.5)
plt.minorticks_on()
plt.ylim(0,5)


plt.savefig('Graph Matplotlib(3-5).jpg')