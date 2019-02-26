import math
n=list(map(float, input().split()))[:2]
a=n[0]
b=n[1]

def poisson2_a(a):
    return(160 + 40*((a+pow(a,2))))

def poisson2_b(b):
    return(128 + 40*(b+pow(b,2)))

print("{0:.3f}".format(poisson2_a(a)))
print("{0:.3f}".format(poisson2_b(b)))

