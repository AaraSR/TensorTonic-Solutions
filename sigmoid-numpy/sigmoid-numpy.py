import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x_np = np.asarray(x, dtype=float)
    return ((1 + np.exp(-x_np)) ** -1)