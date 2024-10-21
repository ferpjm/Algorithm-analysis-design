def contadorCiertos(s):
    cont=0
    for elem in s:
        if(elem==True):
            cont=cont+1
    return cont

def BTMejor(numeros, n, numObjetivo, solucion, sumaQueLLevamos, cuantoQueda, solucionMejor,etapa):
    for intento in range(0,2):
        if (intento==1 and (sumaQueLLevamos[0]+numeros[etapa]<=numObjetivo) or
                (intento == 0 and etapa < n - 1 and (sumaQueLLevamos[0] + cuantoQueda[etapa] > numObjetivo)) or
                (intento == 0 and etapa == n - 1 and (sumaQueLLevamos[0]== numObjetivo))
        ):
            if(intento==0):
                solucion[etapa] = False
            else:
                solucion[etapa] = True
                sumaQueLLevamos[0]=sumaQueLLevamos[0]+numeros[etapa]
            if sumaQueLLevamos[0]==numObjetivo:
                if contadorCiertos(solucion) < contadorCiertos(solucionMejor):
                    for i in range(len(solucion)):
                        solucionMejor[i]=solucion[i]
            else:
                if(etapa<n-1):
                    BTMejor(numeros, n, numObjetivo, solucion, sumaQueLLevamos, cuantoQueda, solucionMejor,etapa+1)

            if(intento==1):
                solucion[etapa] = False
                sumaQueLLevamos[0]=sumaQueLLevamos[0]-numeros[etapa]
n=7
numeros=[5,6,7,9,1,3,2]
numObjetivo=13

solucion=[False]*n
sumaQueLLevamos=[0]
cuantoQueda=[0]*n

acu=0
for i in range(n-1,-1,-1):
    acu=acu+numeros[i]
    cuantoQueda[i]=acu

print (cuantoQueda)

solucionMejor=[True]*n
BTMejor(numeros, n, numObjetivo, solucion, sumaQueLLevamos, cuantoQueda, solucionMejor,0)
print(numeros)
print(solucionMejor)