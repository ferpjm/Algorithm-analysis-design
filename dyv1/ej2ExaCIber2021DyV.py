def DyV(a,ini,fin):
    if ini==fin:
        if(a[ini]==ini):
            return ini
        else:
            return -1
    else:
        mitad=(ini+fin)//2
        if (a[mitad]==mitad):
            return mitad
        elif(a[mitad]>mitad):
            return DyV(a,ini,mitad)
        else:
            return DyV(a,mitad+1,fin)



a=[-3,-1,0,2,4,5,13]
posicion=DyV(a,0,len(a)-1)
print(posicion)