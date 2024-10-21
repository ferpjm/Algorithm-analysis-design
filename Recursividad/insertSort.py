def insertar(a,elem,posicion):
    if a[posicion]>elem:
        a.insert(posicion,elem)
    else:
        if (len(a)>posicion+1):
            insertar(a,elem,posicion+1)
        else:
            a.append(elem)
def insertSort(a,sol):
    if(len(a)>=1):
        if len(a)==1:
            insertar(sol,a[0],0)
        else:
            insertar(sol, a[0],0)
            insertSort(a[1:],sol)

a=[14,0,3,7,11,2,15,4,7,10]
sol=[a[0]]

insertSort(a[1:],sol)
print(sol)