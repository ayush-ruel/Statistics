n = int(input())
a = list(map(int, input().split()))[:n]
b = list(map(int, input().split()))[:n]
sum1 = 0
denosum = 0
for i in range(n):
    sum1 = sum1+(a[i]*b[i])
    denosum = denosum+b[i]
print("{0:.1f}".format(sum1/denosum))
