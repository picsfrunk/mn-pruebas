import numpy as np
from scipy.linalg import solve

def jacobi(A, b, k):
    n = len(b)
    x = np.zeros(n)  # Aproximación inicial de las soluciones
    H = np.zeros((k, n, n))  # Matriz de iteración H
    v = np.zeros((k+1, n))  # Vector v del método de Jacobi en cada iteración
    norm = np.zeros(k)  # Norma de cada iteración

    for i in range(k):
        if i == 0:
            H[i] = np.diag(np.diag(A))  # Diagonal de la matriz A como primera matriz de iteración
        else:
            H[i] = -np.linalg.inv(np.diag(np.diag(A))) @ (A - np.diag(np.diag(A)))  # Matriz de iteración de Jacobi

        v[i+1] = H[i] @ v[i] + np.linalg.inv(np.diag(np.diag(A))) @ b  # Cálculo del vector v en cada iteración
        x = v[i+1]  # Actualización de la aproximación de las soluciones

        norm[i] = np.linalg.norm(A @ x - b)  # Cálculo de la norma de cada iteración

    return H, norm, x

# Matriz de coeficientes
A = np.array([[4, 1, -1],
              [3, 5, 1],
              [1, -2, 6]])

# Vector de términos independientes
b = np.array([5, -2, 7])

# Número de iteraciones
k = 5

# Solución utilizando el método de Jacobi
H, norm, sol_jacobi = jacobi(A, b, k)

# Imprimir las matrices de iteración H y su respectiva norma
for i in range(k):
    print(f"Iteración {i+1}:")
    print("Matriz H:")
    print(H[i])
    print("Norma:", norm[i])
    print()

# Solución exacta utilizando la función solve() de NumPy
sol_exacta = solve(A, b)
print("Solución exacta con solve():", sol_exacta)
