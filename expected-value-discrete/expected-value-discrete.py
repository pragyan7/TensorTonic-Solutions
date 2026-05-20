import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.asarray(x)
    p = np.asarray(p)

    if len(x) != len(p):
        raise ValueError("Length of x and p don't match")
    if not np.isclose(np.sum(p), 1):
        raise ValueError("Probabilities don't sum upto 1")
    return float(np.sum(x*p))
