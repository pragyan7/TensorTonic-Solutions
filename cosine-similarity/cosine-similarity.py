import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.asarray(a)
    b = np.asarray(b)
    
    if a.shape != b.shape:
        raise ValueError("a and b must have the same shape")
    
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    if norm_a == 0 or norm_b == 0:
        # raise ValueError("Cosine similarity is undefined for zero vectors")
        return 0.0
    cs = np.dot(a, b)/(norm_a*norm_b)
    return float(cs)