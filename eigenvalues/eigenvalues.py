import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    mat=np.array(matrix,dtype=float)
    eigen=np.linalg.eigvals(mat)
    ans=np.sort(eigen).real
    return ans
    pass