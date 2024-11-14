import numpy as np

# Definimos la matriz A
A = np.array([
    [1, 0, -4, 1],
    [4, 5, 7, 0],
    [1, -2, 0, 3]
])

# Norma de columnas (||A||_1)
norma_1 = np.max(np.sum(np.abs(A), axis=0))
print("Norma de columnas (||A||_1):", norma_1)

# Norma de Frobenius (||A||_2)
norma_2 = np.sqrt(np.sum(A**2))
print("Norma de Frobenius (||A||_2):", norma_2)

# Norma de filas (||A||_∞)
norma_inf = np.max(np.sum(np.abs(A), axis=1))
print("Norma de filas (||A||_∞):", norma_inf)