def busquedaBinariaRec(a,x,ini,fin):
    if(ini==fin):
        if(a[ini]==x):
            return ini
        else:
            return -1
    else:
        medio = ini+fin//2
        if(a[medio]==x):
            return medio
        if(a[medio]>x):
            return busquedaBinariaRec(a,x,ini,medio)
        else:
            return busquedaBinariaRec(a,x,medio,fin)


def busquedaBinaria(a,x):
    return busquedaBinariaRec(a,x,0,len(a)-1)


a=[2,5,8,10,14,19,34,56,78]
x=14


posicion=busquedaBinaria(a,x)

print(posicion)