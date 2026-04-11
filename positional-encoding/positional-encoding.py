import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    PE=np.zeros((seq_len, d_model))
    for pos in range(seq_len):
        for i in range(0, d_model, 2):
            PE[pos, i]=np.sin(pos/(base**(i/d_model)))
            if i+1<d_model:
                PE[pos, i+1]=np.cos(pos/(base**(i/d_model)))
    return PE
    pass