import numpy as np
import numpy.random as rnd

# Номер 1
rnd.seed(1)

# Номер 2
massiv = rnd.rand(120)

# Номер 3
mas_mean = np.mean(massiv)
mas_srotkl = np.std(massiv)
mas_summ = sum(massiv)

# Номер 4
matrix = massiv.reshape(12, 10)
print(matrix)

# Номер 5
ax0_mean = matrix.mean(axis=0)
ax0_srotkl = matrix.std(axis=0)
ax0_sum = matrix.sum(axis=0)

ax1_mean = matrix.mean(axis=1)
ax1_srotkl = matrix.std(axis=1)
ax1_sum = matrix.sum(axis=1)

# Номер 6
ax1_max = matrix.max(axis=1)
ax1_min = matrix.min(axis=1)

# Номер 7
ax0_argmax = matrix.argmax(axis=0)
ax0_argmin = matrix.argmin(axis=0)
