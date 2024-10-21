def sumatorio(n):
    if n==1:
        return f(1)
    else:
        return f(n)+ sumatorio(n-1)

def f(n):
    if (n==1) or n==2:
        return 1
    else:
        return 1 + sumatorio(n-2)

print(f(10))