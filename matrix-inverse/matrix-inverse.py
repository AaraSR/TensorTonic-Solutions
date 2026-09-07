import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    # Write code here
    A_np = np.asarray(A)

    if np.linalg.det(A) == 0:    # 'A' is singular
        return None
    return np.linalg.inv(A_np)