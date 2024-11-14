import numpy as np

def esta_bien_condicionada(cond, umbral=10):
    """
    Determina si una matriz está bien condicionada.
    Una matriz está bien condicionada si su número de condicionamiento es menor al umbral.
    """
    return cond < umbral

def main():
    # Matrices A y B
    A = np.array([
        [1/3, 1],
        [1, 3]
    ])
    B = np.array([
        [4, 4],
        [3, 5]
    ])

    # 2.1 Normas
    norma_A_2 = np.linalg.norm(A, ord='fro')  # Norma de Frobenius para A
    norma_B_2 = np.linalg.norm(B, ord='fro')  # Norma de Frobenius para B

    if np.linalg.det(A) != 0:
        norma_inv_A_2 = np.linalg.norm(np.linalg.inv(A), ord='fro')  # Norma de la inversa de A
    else:
        norma_inv_A_2 = float('inf')  # No tiene inversa

    norma_inv_B_2 = np.linalg.norm(np.linalg.inv(B), ord='fro')  # Norma de la inversa de B

    print("Norma de frobenius de A:", norma_A_2)
    print("Norma de frobenius de B:", norma_B_2)
    print("Norma de frobenius de A^-1:", norma_inv_A_2)
    print("Norma de frobenius de B^-1:", norma_inv_B_2)

    # 2.2 Número de condicionamiento
    cond_A = np.linalg.cond(A, p='fro')
    cond_B = np.linalg.cond(B, p='fro')
    print("\nNúmero de condicionamiento de A:", cond_A)
    print("Número de condicionamiento de B:", cond_B)

    # 2.3 Determinantes
    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)
    print("\nDeterminante de A:", det_A)
    print("Determinante de B:", det_B)

    #Pequeñez v del determinante
    n_A = A.shape[0]
    n_B = B.shape[0]

    v_A = abs(det_A) / (norma_A_2**n_A) if det_A != 0 else 0
    v_B = abs(det_B) / (norma_B_2**n_B) if det_B != 0 else 0

    print("\nPequeñez v de A:", v_A)
    print("Pequeñez v de B:", v_B)
    
    # 2.4 Evaluar si las matrices están bien condicionadas
    umbral = 10
    print("\n¿La matriz A está bien condicionada?", "Sí" if esta_bien_condicionada(cond_A, umbral) else "No")
    print("¿La matriz B está bien condicionada?", "Sí" if esta_bien_condicionada(cond_B, umbral) else "No")




if __name__ == "__main__":
    main()
