import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    x_np = np.asarray(x, dtype=float)
    y_np = np.asarray(y, dtype=float)

    return float( np.sqrt( np.sum( np.square(x_np - y_np) ) ) )