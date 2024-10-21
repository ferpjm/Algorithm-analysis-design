def busquedaBinaria(a,x):
    if(len(a)==1):
        if(a[0]==x):
            return 0
        else:
            return -1
    else:
        medio = len(a)//2
        if(a[medio]==x):
            return medio
        elif(a[medio]>x):
            return busquedaBinaria(a[:medio],x)
        else:
            aux=busquedaBinaria(a[medio:],x)
            if(aux==-1):
                return aux
            else:
                return medio + aux


a = [2, 5, 8, 10,14,19,34,56,78]
elem = int(input())

print(busquedaBinaria(a, elem))