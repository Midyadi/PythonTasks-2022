import numpy as np

# Номер 1
vec = np.arange(1,100)

# Номер 2
print(vec[::3])

# Номер 3
trios = np.array([sum(vec[i:i+3]) for i in range(0,len(vec),3)])

# Номер 4
matrix = trios.reshape(11,3)

# Номер 5
transponded_matrix = matrix.T

# Номер 6
new_vec = np.arange(-9,2)
transponded_matrix.dot(new_vec)

# Номер 7
srez = transponded_matrix[::2,1::4]
with open('matrix for numpy(7).dat', 'w') as mat:
    for line in srez:
        print(*line,file=mat)

# Номер 8
new_matrix = matrix[2:9:3]
determinant = np.linalg.det(new_matrix)
