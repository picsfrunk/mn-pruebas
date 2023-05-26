import numpy as np

def jacobi_table(A, b, max_iterations, tolerance):
    n = len(A)
    x = np.zeros(n)  # Aproximación inicial de las soluciones
    iterations = 0

    print("Método de Jacobi - Solución de un sistema de ecuaciones lineales")
    print("----------------------------------------------------------------")
    print("Matriz de coeficientes (A):")
    print(np.round(A, 6))
    print("\nVector de términos independientes (b):")
    print(np.round(b, 6))
    print("\nAproximación inicial de las soluciones (x):")
    print(np.round(x, 6))

    while iterations < max_iterations:
        iterations += 1
        x_new = np.zeros_like(x)

        for i in range(n):
            sum_term = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum_term) / A[i, i]

        if np.linalg.norm(x - x_new) < tolerance:
            break

        x = x_new

        print("\n--------------------------------------")
        print(f"Iteración {iterations}:")
        print("--------------------------------------")
        print("Aproximación actual de las soluciones (x):")
        print(np.round(x, 6))

    print("\n--------------------------------------")
    print("Solución encontrada:")
    print("--------------------------------------")
    print("Valores de las incógnitas:")
    print(f"x = {np.round(x[0], 6)}, y = {np.round(x[1], 6)}, z = {np.round(x[2], 6)}")

# Matriz de coeficientes
A = np.array([[4, 1, -1],
              [3, 5, 1],
              [1, -2, 6]])

# Vector de términos independientes
b = np.array([5, -2, 7])

# Parámetros del método de Jacobi
max_iterations = 5
tolerance = 1e-6

# Ejecución del método de Jacobi y visualización de los resultados en forma de tabla
jacobi_table(A, b, max_iterations, tolerance)
