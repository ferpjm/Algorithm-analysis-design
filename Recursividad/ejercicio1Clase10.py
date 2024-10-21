def ejercicio1(a):
    if len(a)<2:
        return []
    else:
        return [a[0]+a[1]] + ejercicio1(a[1:])


a=[1,5,10,-2,1]
print(ejercicio1(a))