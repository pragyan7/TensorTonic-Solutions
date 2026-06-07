import numpy as np
import math

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x = np.sort(np.array(x).flatten())
    q = np.array(q).flatten()
    n = len(x)
    ans = []

    for p in q:
        index = (p/100) * (n-1)

        lower = math.floor(index)
        upper = math.ceil(index)

        if lower == upper:
            value = x[lower]
        else:
            fraction = index - lower
            value = x[lower] + fraction * (x[upper] - x[lower])
        ans.append(value)
    return np.array(ans)