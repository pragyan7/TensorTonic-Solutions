import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows = len(A)
    cols = len(A[0])

    A_T = [[0]*rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            A_T[j][i] = A[i][j]
    return np.array(A_T)
