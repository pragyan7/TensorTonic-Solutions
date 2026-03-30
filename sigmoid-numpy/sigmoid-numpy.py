import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x) #convert list to array
    return (1 / (1 + np.exp(-x)))