import numpy as np

def calcular_pequenez(det, norma, n):
    """
    Calcula la pequeñez v del determinante.
    Si el determinante es cero, devuelve cero.
    """
    return abs(det) / (norma**n) if det != 0 else 0

def esta_bien_condicionada(cond, umbral=10):
    """
    Determina si una matriz está bien condicionada.
    Una matriz está bien condicionada si su número de condicionamiento es menor al umbral.
    """
    return cond < umbral

def main():
    # Nuevas matrices A y B
    A = np.array([
        [1, 4],
        [2/9, 1]
    ])
    B = np.array([
        [3, 5],
        [-2, 2]
    ])

    # 3.1 Normas
    norma_A_2 = np.linalg.norm(A, ord='fro')  # Norma de Frobenius para A
    norma_B_2 = np.linalg.norm(B, ord='fro')  # Norma de Frobenius para B
    norma_inv_A_2 = np.linalg.norm(np.linalg.inv(A), ord='fro')  # Norma de la inversa de A
    norma_inv_B_2 = np.linalg.norm(np.linalg.inv(B), ord='fro')  # Norma de la inversa de B

    print("Norma de frobenius de A:", norma_A_2)
    print("Norma de frobenius de B:", norma_B_2)
    print("Norma de frobenius de A^-1:", norma_inv_A_2)
    print("Norma de frobenius de B^-1:", norma_inv_B_2)

    # 3.2 Número de condicionamiento
    cond_A = np.linalg.cond(A, p='fro')  # Número de condicionamiento para A
    cond_B = np.linalg.cond(B, p='fro')  # Número de condicionamiento para B
    print("\nNúmero de condicionamiento de A:", cond_A)
    print("Número de condicionamiento de B:", cond_B)

    # 3.3 Determinantes
    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)
    print("\nDeterminante de A:", det_A)
    print("Determinante de B:", det_B)

    # Pequeñez v del determinante
    n_A = A.shape[0]
    n_B = B.shape[0]

    v_A = calcular_pequenez(det_A, norma_A_2, n_A)
    v_B = calcular_pequenez(det_B, norma_B_2, n_B)

    print("\nPequeñez v de A:", v_A)
    print("Pequeñez v de B:", v_B)
    
    # 3.4 Evaluar si las matrices están bien condicionadas
    umbral = 10
    print("\n¿La matriz A está bien condicionada?", "Sí" if esta_bien_condicionada(cond_A, umbral) else "No")
    print("¿La matriz B está bien condicionada?", "Sí" if esta_bien_condicionada(cond_B, umbral) else "No")

if __name__ == "__main__":
    main()
