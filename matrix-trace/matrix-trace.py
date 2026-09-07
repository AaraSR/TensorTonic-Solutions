import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    A_np = np.asarray(A)

    return float(np.linalg.trace(A_np))