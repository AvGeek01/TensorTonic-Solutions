import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    row, col=len(A), len(A[0])
    transpose=[[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            transpose[j][i]=A[i][j]
    return np.array(transpose)
    pass
