from math import factorial, ceil

def kperm(n, k):
    out = []
    first = ceil(k / factorial(n - 1))
    out.append(first)
    kperm(n - 1, 

