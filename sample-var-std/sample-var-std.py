import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    ans={}
    cc=x-np.mean(x)
    variance=np.sum(cc**2)/(len(x)-1)
    ans["variance"]=float(variance)
    ans["standard_deviation"]=float(np.sqrt(variance))
    return ans
    pass