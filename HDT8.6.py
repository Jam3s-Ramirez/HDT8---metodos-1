import numpy as np

def main():
    # 6.1 Solución del primer sistema de ecuaciones
    print("6.1 Solución exacta del primer sistema:")
    A1 = np.array([
        [-0.10, 1.00],
        [0.11, -1.00]
    ])
    b1 = np.array([-2.0, 2.1])

    # Solución exacta
    x1 = np.linalg.solve(A1, b1)
    print("Solución del primer sistema: x =", x1[0], ", y =", x1[1])

    # 6.2 Solución del segundo sistema de ecuaciones
    print("\n6.2 Solución exacta del segundo sistema:")
    A2 = np.array([
        [-0.10, 1.00],
        [0.11, -1.00]
    ])
    b2 = np.array([-2.00, 2.14])

    # Solución exacta
    x2 = np.linalg.solve(A2, b2)
    print("Solución del segundo sistema: x =", x2[0], ", y =", x2[1])

    # 6.3 Condición del sistema (número de condición)
    print("\n6.3 Análisis de condición del sistema:")
    cond_A1 = np.linalg.cond(A1)  # Número de condición de la matriz A1
    print("Número de condición del sistema 6.1 (κ):", cond_A1)

    # Relación con determinante y eigenvalores
    print("\n6.4 Relación entre κ, determinante y eigenvalores:")
    det_A1 = np.linalg.det(A1)
    eigenvalues_A1 = np.linalg.eigvals(A1)

    print("Determinante de la matriz A1:", det_A1)
    print("Eigenvalores de la matriz A1:", eigenvalues_A1)

    # Para el sistema A2
    cond_A2 = np.linalg.cond(A2)
    det_A2 = np.linalg.det(A2)
    eigenvalues_A2 = np.linalg.eigvals(A2)

    print("\nNúmero de condición del sistema 6.2 (κ):", cond_A2)
    print("Determinante de la matriz A2:", det_A2)
    print("Eigenvalores de la matriz A2:", eigenvalues_A2)

    # Análisis final
    print("\nAnálisis:")
    print("Un sistema con un número de condición elevado (κ grande) es mal condicionado, lo que indica que pequeños cambios en los datos pueden provocar grandes cambios en la solución.")
    print("El determinante pequeño y la cercanía de los eigenvalores a cero también contribuyen a la inestabilidad del sistema.")

if __name__ == "__main__":
    main()
