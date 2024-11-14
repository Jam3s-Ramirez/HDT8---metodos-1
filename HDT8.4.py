import numpy as np

def main():
    # Nuevas matrices A y B
    A = np.array([
        [1/3, 1],
        [1, 3]
    ])
    B = np.array([
        [1, 4],
        [2/9, 1]
    ])

    # Uso de norma infinito
    norma_A_inf = np.linalg.norm(A, ord=np.inf)
    norma_B_inf = np.linalg.norm(B, ord=np.inf)

    # Verificar si las matrices tienen inversa antes de calcular normas de la inversa
    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)

    if det_A != 0:
        norma_inv_A_inf = np.linalg.norm(np.linalg.inv(A), ord=np.inf)
    else:
        norma_inv_A_inf = float('inf')  # Inversa no definida

    if det_B != 0:
        norma_inv_B_inf = np.linalg.norm(np.linalg.inv(B), ord=np.inf)
    else:
        norma_inv_B_inf = float('inf')  # Inversa no definida

    # Imprimir resultados
    print("Norma infinito de A2.4:", norma_A_inf)
    print("Norma infinito de A3.4:", norma_B_inf)
    print("Norma infinito de A2.4^-1:", "No definida" if det_A == 0 else norma_inv_A_inf)
    print("Norma infinito de B3.4^-1:", "No definida" if det_B == 0 else norma_inv_B_inf)
    print("Los resultados sí cambian a combian a comparación de los resultados de los ejercicios 2.4 y 3.4")

if __name__ == "__main__":
    main()
