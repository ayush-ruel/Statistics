a=list(map(int, input().split()))[:2]
n=int(input())
p=a[0]/a[1]
def geometric1(n,p):
    return ((1-p)**(n-1)*p)
print("{0:.3f}".format(geometric1(n,p)))

