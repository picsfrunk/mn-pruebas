import numpy as np
import matplotlib.pyplot as plt

# Datos de velocidad y fuerza de fricción
v = np.array([1, 2, 3, 4, 5])
f = np.array([5, 15.3, 29.3, 46.4, 66.3])

# Aproximación lineal
coeff_linear = np.polyfit(v, f, 1)
f_linear = np.poly1d(coeff_linear)

# Aproximación cuadrática
coeff_quad = np.polyfit(v, f, 2)
f_quad = np.poly1d(coeff_quad)

# Graficar los puntos y las aproximaciones
plt.scatter(v, f, color='blue', label='Puntos')
plt.plot(v, f_linear(v), color='red', label='Aproximación lineal')
plt.plot(v, f_quad(v), color='green', label='Aproximación cuadrática')
plt.xlabel('Velocidad (cm/s)')
plt.ylabel('Fuerza de fricción (10^6 dinas)')
plt.legend()
plt.show()

# Imprimir las funciones encontradas
print("Aproximación lineal:")
print(f_linear)

print("\nAproximación cuadrática:")
print(f_quad)
