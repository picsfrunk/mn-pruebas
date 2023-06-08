import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Crear la figura y los subplots
fig, axes = plt.subplots(3, 1, figsize=(8, 12))

# Configurar el primer subplot
axes[0].plot(x, y1, color='red')
axes[0].set_title('Seno')

# Configurar el segundo subplot
axes[1].plot(x, y2, color='green')
axes[1].set_title('Coseno')

# Configurar el tercer subplot
axes[2].plot(x, y3, color='blue')
axes[2].set_title('Tangente')

# Ajustar el espaciado entre subplots
plt.tight_layout()

# Mostrar la figura con los subplots
plt.show()
