import math
arr=list(map(int, input().split()))[:2]
p=arr[0]/100
n=arr[1]
pltt=0
palt=0

def binomial(x,n,p):
    f=math.factorial
    return ((f(n)/( f(x) * f(n-x)))*(p**x)*((1-p)**(n-x)))

for i in range (3):
    pltt += (binomial(i,n,p))

for i in range (2,n):
    palt += (binomial(i,n,p))

print("{0:.3f}".format(pltt))
print("{0:.3f}".format(palt))
