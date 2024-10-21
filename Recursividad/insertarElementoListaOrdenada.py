def insertar(sol,a,elem):
    if a[0]>elem:
        sol.append(elem)
        return sol+a
    else:
        sol.append(a[0])
        if (len(a)==1):
            sol.append(elem)
            return sol
        else:
            return insertar(sol,a[1:],elem)


sol=[]
a=[-3,0,3,8,11]
elem=50

print(insertar(sol,a,elem))