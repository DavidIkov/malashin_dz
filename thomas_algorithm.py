import numpy as np

def solve(A, B, C, D):
    """
    Решение трехдиагональной системы методом прогонки
    """
    n = len(D)
    
    # Прямой ход - вычисление прогоночных коэффициентов
    alpha = np.zeros(n)
    beta = np.zeros(n)
    
    alpha[0] = -C[0] / B[0]
    beta[0] = D[0] / B[0]
    
    for i in range(1, n):
        denominator = B[i] + A[i] * alpha[i-1]
        alpha[i] = -C[i] / denominator
        beta[i] = (D[i] - A[i] * beta[i-1]) / denominator
    
    # Обратный ход
    y = np.zeros(n)
    y[n-1] = beta[n-1]
    
    for i in range(n-2, -1, -1):
        y[i] = alpha[i] * y[i+1] + beta[i]
    
    return y
