import numpy as np
import matplotlib.pyplot as plt

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

fig, ax = plt.subplots()

ax.imshow(matriz, cmap='viridis')

# Agregar los valores de la matriz en cada posición
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        ax.text(j, i, str(matriz[i, j]), ha='center', va='center', color='white')

plt.show()
