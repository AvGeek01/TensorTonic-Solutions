import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    ans={}
    probab=[]
    for i in range(k+1):
        prob=(math.exp(-lam)*(lam**i))/math.factorial(i)
        probab.append(prob)
    pmf=probab[k]
    cdf=sum(probab)
    ans["pmf"]=pmf
    ans["cdf"]=cdf
    return ans
    pass