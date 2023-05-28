def jacobi_table(A, b, max_iterations):
    # Parámetros del método de Jacobi
    tolerance = 1e-4
    n = len(A)
    x = np.zeros(n)  # Aproximación inicial de las soluciones
    iterations = 0

    # Imprimir los datos iniciales del sistema de ecuaciones
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

        # Calcular la nueva aproximación de las soluciones
        for i in range(n):
            sum_term = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - sum_term) / A[i, i]

        if np.linalg.norm(x - x_new) < tolerance:
            break

        x = x_new

        # Imprimir la aproximación actual de las soluciones en cada iteración
        print("\n--------------------------------------")
        print(f"Iteración {iterations}:")
        print("--------------------------------------")
        print("Aproximación actual de las soluciones (x):")
        print(np.round(x, 6))

    # Imprimir la solución final con los valores de las incógnitas
    print("\n--------------------------------------")
    print("Solución encontrada:")
    print("--------------------------------------")
    print("Valores de las incógnitas:")
    print(f"x = {np.round(x[0], 6)}, y = {np.round(x[1], 6)}, z = {np.round(x[2], 6)}")
