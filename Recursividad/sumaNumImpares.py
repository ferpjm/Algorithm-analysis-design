def sumNumImpares(n):
    if n==1:
        return 2*n-1
    else:
        return 2*n-1+sumNumImpares(n-1)

n=10
print(sumNumImpares(n))