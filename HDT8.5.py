import numpy as np

# Definir la matriz A
A = np.array([
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
])

# Inciso 5.1: Calcular el número de condición de la matriz A
def calcular_numero_de_condicion(matrix):
    kappa = np.linalg.cond(matrix)
    return kappa

# Inciso 5.2: Calcular el determinante de la matriz A
def calcular_determinante(matrix):
    determinante = np.linalg.det(matrix)
    return determinante

# Inciso 5.3: Evaluar la pequeñez del determinante
def evaluar_pequenez_determinante(determinante):
    if abs(determinante) < 1e-3:  # Umbral para considerar pequeñez
        return "El determinante es pequeño, la matriz podría estar cerca de ser singular."
    else:
        return "El determinante no es pequeño."

# Inciso 5.4: Determinar relación entre el número de condición y los eigenvalores
def analizar_eigenvalores(matrix):
    eigenvalores = np.linalg.eigvals(matrix)
    relacion = "Número de condición alto implica eigenvalores cercanos o valores pequeños, lo que sugiere una matriz mal condicionada."
    return eigenvalores, relacion

# Llamadas a las funciones para obtener los resultados
kappa = calcular_numero_de_condicion(A)
determinante = calcular_determinante(A)
pequenez_determinante = evaluar_pequenez_determinante(determinante)
eigenvalores, relacion = analizar_eigenvalores(A)

# Mostrar los resultados
print("5.1: Número de condición de A:", kappa)
print("5.2: Determinante de A:", determinante)
print("5.3:", pequenez_determinante)
print("5.4: Eigenvalores de A:", eigenvalores)
print("Relación entre condición y eigenvalores:", relacion)

