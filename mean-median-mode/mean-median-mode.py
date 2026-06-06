import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.asarray(x)
    mean = float(np.mean(x))
    median = float(np.median(x))

    frequency = Counter(x)
    mode = float(frequency.most_common(1)[0][0])

    return (mean, median, mode)