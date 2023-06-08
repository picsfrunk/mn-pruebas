import numpy as np
import matplotlib.pyplot as plt

def calcular_recta_mejor_ajuste(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x**2)
    
    # Calculamos la pendiente (b) y el intercepto (a) de la recta de mejor ajuste
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    a = (sum_y - b * sum_x) / n
    
    return a, b

def calcular_error_cuadratico(x, y, a, b):
    y_pred = a + b * x
    error_cuadratico = np.sum((y - y_pred)**2)
    return error_cuadratico

# Leer los puntos en R2
n = int(input("Ingrese el número de puntos: "))
x = np.zeros(n)
y = np.zeros(n)

for i in range(n):
    x[i] = float(input(f"Ingrese la coordenada x del punto {i+1}: "))
    y[i] = float(input(f"Ingrese la coordenada y del punto {i+1}: "))

# Calcular la recta de mejor ajuste
a, b = calcular_recta_mejor_ajuste(x, y)

# Calcular el error cuadrático
error_cuadratico = calcular_error_cuadratico(x, y, a, b)

# Graficar los puntos y la recta de mejor ajuste
plt.scatter(x, y, color='blue', label='Puntos')
plt.plot(x, a + b * x, color='red', label='Recta de mejor ajuste')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Imprimir resultados
print(f"La recta de mejor ajuste es: Y = {a} + {b} * X")
print(f"El error cuadrático total es: {error_cuadratico}")
