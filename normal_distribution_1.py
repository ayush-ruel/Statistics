import math
n=list(map(int, input().split()))[:2]
mean=n[0]
standardDeviation=n[1]
q1=float(input())
q2=list(map(int, input().split()))[:2]
ll=q2[0]
ul=q2[1]

def normal(x):
    return 0.5 * (1 + math.erf((x - mean) / (standardDeviation * (2 ** 0.5))))

print("{0:.3f}".format(normal(q1)))
print("{0:.3f}".format(normal(ul)-normal(ll)))
