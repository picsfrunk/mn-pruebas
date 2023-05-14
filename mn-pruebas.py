import numpy as np

def jacobi(A, b, k):
    n = A.shape[0]
    x = np.zeros(n)  # Vector inicial de ceros
    H = np.zeros((k, n))  # Matriz de iteración
    norms = np.zeros(k)  # Normas de las matrices de iteración
    v = np.zeros((k, n))  # Vectores resultantes en cada paso

    for i in range(k):
        x_new = np.zeros(n)
        for j in range(n):
            x_new[j] = (b[j] - np.dot(A[j, :j], x[:j]) - np.dot(A[j, j+1:], x[j+1:])) / A[j, j]
        H[i] = x_new
        norms[i] = np.linalg.norm(H[i])
        v[i] = x_new
        x = x_new

    return H, norms, v

# Lectura de datos de entrada
n = int(input("Ingrese el tamaño de la matriz cuadrada (n >= 1): "))
A = np.zeros((n, n))
print("Ingrese los elementos de la matriz A:")
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"A[{i+1},{j+1}]: "))

b = np.zeros(n)
print("Ingrese los elementos del vector b:")
for i in range(n):
    b[i] = float(input(f"b[{i+1}]: "))

k = int(input("Ingrese el número de iteraciones (k >= 0): "))

# Aplicación del método de Jacobi
H, norms, v = jacobi(A, b, k)

# Mostrar resultados
print("\nMatriz de iteración H:")
print(H)

print("\nNormas de las matrices de iteración:")
print(norms)

print("\nVectores v en cada paso:")
print(v)
