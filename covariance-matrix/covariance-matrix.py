import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    try:
        X = np.asarray(X, dtype=float)
    except:
        raise (ValueError, TypeError)
        return None

    if X.ndim != 2:
        return None
        
    N = X.shape[0]
    if N < 2:
        return None

    mu = np.mean(X, axis=0)

    X_centered = X - mu

    cov = (X_centered.T @ X_centered) / (N-1)
    return cov