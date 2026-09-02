import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    cc=x-np.mean(x)
    variance=np.sum(cc**2)/(len(x)-1)
    std=np.sqrt(variance)
    std_err=std/np.sqrt(len(x))
    t=(np.mean(x)-mu0)/std_err
    return float(t)
    pass