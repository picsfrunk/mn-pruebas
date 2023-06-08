import numpy as np
import matplotlib.pyplot as plt

def differences_divided(x, y):
    n = len(x)
    coefficients = np.copy(y)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i-1]) / (x[i] - x[i-j])
    return coefficients

# Definir los pares de números
x = np.linspace(-5, 5, 20)
y = np.sin(x)
print("x")
print(x)
print("y")
print(y)

# Calcular los coeficientes del polinomio mediante diferencias divididas
coefficients = differences_divided(x, y)

# Crear una función polinómica a partir de los coeficientes
def polynomial(coefficients, x):
    n = len(coefficients)
    result = coefficients[n-1]
    for i in range(n-2, -1, -1):
        result = result * (x - x[i]) + coefficients[i]
    return result

# Crear puntos para graficar la función interpolada
x_interpolated = np.linspace(-5, 5, 100)
y_interpolated = polynomial(coefficients, x_interpolated)
print("y_interpo")
print(y_interpolated)
print("x_interpo")
print(x_interpolated)

# Graficar los puntos y el polinomio interpolado
plt.scatter(x, y, label='Puntos')
plt.plot(x_interpolated, y_interpolated, label='Polinomio Interpolado')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de Diferencias Divididas')
plt.legend()
plt.grid(True)
plt.show()
