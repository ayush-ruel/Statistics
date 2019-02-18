from statistics import median
x=int(input())
c=[0]*(n)
a=list(map(int, input().split()))[:x]
b=list(map(int, input().split()))[:x]
for i in range(x):
    for j in range(b[i]):
        c[j]=a[i]*b[i]
s=c.sort()
t=int(len(a)/2)
if len(a)%2==0:
    L=arr[:t]
    U=arr[t:]
else:
    L=arr[:t]
    U=arr[t+1:]

print(int(median(L))-int(median(U)))
