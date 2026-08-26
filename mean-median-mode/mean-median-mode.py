from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    ans={}
    ans["mean"]=float(np.mean(x))
    ans["median"]=float(np.median(x))
    frq=Counter(x)
    common=frq.most_common(1)[0]
    ans["mode"]=float(common[0])
    return ans
    pass