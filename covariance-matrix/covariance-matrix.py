import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X=np.array(X,dtype=float)
    centre=X-np.mean(X,axis=0)
    cov=(centre.T @ centre)/(X.shape[0]-1)
    return cov
    pass