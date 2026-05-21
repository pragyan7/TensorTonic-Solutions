import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.array(A)
    trace = 0
    diagonal_elements = A.shape[1]
    for i in range(diagonal_elements):
        trace += A[i][i]
        
    return trace
