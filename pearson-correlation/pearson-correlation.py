import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X=np.array(X,dtype=float)
    n=X.shape[0]
    centre=X-np.mean(X,axis=0)
    covariance=(centre.T @ centre)/(n-1)
    std=np.sqrt(np.diag(covariance))
    denominator=np.outer(std,std)
    with np.errstate(divide='ignore',invalid='ignore'):
        correlation=covariance/denominator
    return correlation
    pass