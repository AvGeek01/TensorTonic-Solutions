import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    ans={}
    probabilities=[]
    for i in range(k+1):
        prob=(math.comb(n,i)*(p**i)*((1-p)**(n-i)))
        probabilities.append(prob)
    ans["pmf"]=float(probabilities[k])
    ans["cdf"]=float(sum(probabilities))
    return ans
    pass