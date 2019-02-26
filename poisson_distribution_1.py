import math
m=float(input())
n=int(input())
ans = 0

def poisson(k,lam):
    f=math.factorial
    return (((lam)**k * math.exp(-lam))/f(k))


print("{0:.3f}".format(poisson(n,m)))

