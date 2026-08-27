import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    np.asarray(x,dtype=float)
    return float(np.dot(x,p))
    pass