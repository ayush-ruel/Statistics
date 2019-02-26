import math
arr=list(map(int, input().split()))[:2]
n=int(input())
p=arr[0]/arr[1]
ans = 0

def geometric2(x,n,p):
    f=math.factorial
    return ((f(n)/( f(x) * f(n-x)))*(p**x)*((1-p)**(n-x)))

for i in range (1,n+1):
    ans += (geometric2(i,n,p))

print("{0:.3f}".format(ans))

