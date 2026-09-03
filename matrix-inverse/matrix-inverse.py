import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    matrix=np.array(A,dtype=float)
    n=matrix.shape[0]
    aug=np.concatenate((matrix,np.eye(n)),axis=1)
    for col in range(n):
        pivot_row=col+np.argmax(np.abs(aug[col:,col]))
        if np.isclose(aug[pivot_row,col],0):
            return None
        if pivot_row!=col:
            aug[[col,pivot_row]]=aug[[pivot_row,col]]
        pivot=aug[col,col]
        aug[col]=aug[col]/pivot
        for row in range(n):
            if row!=col:
                factor=aug[row,col]
                aug[row]=(aug[row]-factor*aug[col])
    return aug[:,n:]
    pass