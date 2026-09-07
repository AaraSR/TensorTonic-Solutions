import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a_np = np.asarray(a)
    b_np = np.asarray(b)

    den = np.linalg.norm(a) * np.linalg.norm(b)

    if den != 0:
        return (float(np.dot(a, b)) / float(den))
    else:
        return 0.0