import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    weight = np.linalg.inv(X.T @ X) @ X.T @ y
    
    return weight