import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    
    x=np.array(x,dtype=float)
    keep_prob=1-p
    if keep_prob==0:
        mask=np.zeros_like(x)
        return np.zeros_like(x), mask
    if keep_prob==1:
        mask=np.ones_like(x)
        return x, mask
    if rng is None:
        rng=np.random.default_rng()
    rand_vals=rng.random(x.shape)
    mask=(rand_vals<keep_prob).astype(float)
    mask=mask/keep_prob
    out=x*mask
    return out,mask
    pass