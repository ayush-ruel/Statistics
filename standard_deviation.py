n=int(input())
x=0
a = list(map(int, input().split()))[:n]
b = [0]*(n)
for i in range(n):
    x = x+a[i]
mean1 = (x/n)
for i in range(n):
    b[i] = (a[i]-mean1)**2
print("{0:.1f}".format(((sum(b)/n)**0.5)))
