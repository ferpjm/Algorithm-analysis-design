def DyV(vector,ini,fin):
    if (ini==fin):
        #CONQUISTA
        return [vector[ini],vector[fin]]
    else:
        #DIVISION
        medio = (ini+fin)//2
        [menor1,mayor1] = DyV(vector,ini,medio)
        [menor2,mayor2] = DyV(vector,medio+1,fin)
        #COMBINACION
        menor=min(menor1,menor2)
        mayor=max(mayor1,mayor2)
        return [menor,mayor]
vector = [2,1,3,8,4,10,7,6]
[menor,mayor] =DyV(vector,0,len(vector)-1)
print("El mayor es:", mayor)
print("El menor es:", menor)