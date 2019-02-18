import numpy as np
from scipy import stats 

x=int(input())
sum1 = 0

arr=list(map(int, input().split()[:x]))
for i in range(x):
    sum1 = sum1+arr[i]
print(sum1/x)

print(np.median(arr))
m=stats.mode(arr)

print(int(m[0]))
