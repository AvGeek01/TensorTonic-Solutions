import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    ans={}
    x=np.array(x)
    ans["pmf"]=np.where(x==1,p,1.0-p)
    ans["mean"]=float(p)
    cc=x-np.mean(x)
    ans["variance"]=float(p*(1.0-p))
    return ans
    pass