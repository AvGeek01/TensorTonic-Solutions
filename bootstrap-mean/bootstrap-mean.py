import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    ans={}
    x=np.array(x,dtype=float)
    rng=np.random.default_rng(seed)
    n=len(x)
    indices=rng.integers(0,n,size=(n_bootstrap,n))
    samples=x[indices]
    bootstrap_mean=np.mean(samples,axis=1)
    bootstrap_mean_value=np.mean(bootstrap_mean)
    alpha=1-ci
    lower_percentile=(alpha/2)*100
    upper_percentile=(1-alpha/2)*100
    lower=np.percentile(bootstrap_mean,lower_percentile)
    upper=np.percentile(bootstrap_mean,upper_percentile)
    ans["bootstrap_mean"]=float(bootstrap_mean_value)
    ans['lower']=float(lower)
    ans['upper']=float(upper)
    return ans
    pass