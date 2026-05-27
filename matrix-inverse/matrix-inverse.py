import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    try:
        A = np.asarray(A, dtype=float)
    except Exception:
        return None
        
    if A.ndim!=2:
        return None
        
    if A.shape[0]!=A.shape[1]:
        return None
    
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return None