def DyV(vector,ini,fin):
    if(ini==fin):
        if(vector[ini]%2==0):
            return ini
        else:
            return -1
    else:
        mitad=(ini+fin)//2
        if(vector[mitad]%2 != 0):
            return DyV(vector,ini,mitad)
        else:
            pos= DyV(vector,mitad+1,fin)
            if(pos==-1):
                return mitad
            else:
                return pos




vector=[4,2,6,18,7,9]
posicion =DyV(vector,0,len(vector)-1)
print(posicion)

