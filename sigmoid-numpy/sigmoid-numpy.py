import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    x_np = np.asarray(x)
    return (1 + (np.exp(-x_np)))**(-1)
    