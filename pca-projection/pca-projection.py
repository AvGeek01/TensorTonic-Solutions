import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    X=np.array(X,dtype=float)
    Xc=X-np.mean(X,axis=0)
    n=X.shape[0]
    C=(Xc.T @ Xc)/(n-1)
    eigenval,eigenvec=np.linalg.eigh(C)
    indices=np.argsort(eigenval)[::-1]
    W=eigenvec[:,indices[:k]]
    projected=Xc @ W
    return projected.tolist()
    pass